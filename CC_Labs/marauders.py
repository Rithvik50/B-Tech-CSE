#  _____   ____    _   _  ____ _______   ______ _____ _____ _______
# |  __ \ / __ \  | \ | |/ __ \__   __| |  ____|  __ \_   _|__   __|
# | |  | | |  | | |  \| | |  | | | |    | |__  | |  | || |    | |
# | |  | | |  | | | . ` | |  | | | |    |  __| | |  | || |    | |
# | |__| | |__| | | |\  | |__| | | |    | |____| |__| || |_   | |
# |_____/ \____/  |_| \_|\____/  |_|    |______|_____/_____|  |_|
import json
import subprocess
import time
import re
import requests
import sys


# BASE_URL = "http://localhost:8080"
BASE_URL = "https://maraudersmap.smuz.me"
BORE_BASE_URL = "bore.smuz.me"

print("Welcome to Marauders!\n")

print("This is an automatic evaluator for CC labs. We will check that you have done the steps as you as doing them.")
print("Which means you don't have to take screenshots anymore, Hurray!\n")

print("Make sure to come back here and hit enter after every step to proceed.")
print("Please remember to do this as in the worst case if you forget you might have to redo the whole labs\n")

print("===This is a new tool and we are testing it out. If you find any issues, please contact your nearest TA!===\n")

SRN = str(input("Please Input your SRN: ")).strip().lower()
LAB_NUM_STR = input("Please Enter Lab Number: ")

try:
    LAB_NUM = int(LAB_NUM_STR)
    print()
except ValueError:
    print("Error: Lab Number must be an Integer")
    sys.exit()

tunnels_resp = requests.get(f"{BASE_URL}/lab/{LAB_NUM}/tunnels")
if tunnels_resp.status_code != 200:
    print("Something went wrong getting the lab. Are you sure you have entered a valid lab number?")
    print(f"Status Code: {tunnels_resp.status_code}, Response Body: {str(tunnels_resp.content)}")
    sys.exit()
tunnels = tunnels_resp.json()

# Function to handle graceful shutdown
def graceful_shutdown(processes):
    print("\nShutting down tunnels...")
    for process in processes:
        process.terminate()
    for process in processes:
        process.wait()
    print("Tunnels stopped. Exiting program.")
    exit(0)

def start_tunnel(service_name, protocol, port):
    command = ['bore', 'local', str(port), "--to", BORE_BASE_URL]

    print(f"Starting bore tunnel for {service_name} on port {port}")
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output_dirty = process.stdout.readline()
    # print(output_dirty)
    output = re.sub(r'\x1b\[[0-9;]*m', '', output_dirty)
    # print(output)

    # Extract port number using regex
    match = re.search(r"remote_port=(\d+)", output)
    if match:
        port = match.group(1)
        return process, port
    else:
        print(f"Could not establish a bore tunnel to port {port}. Please contact a TA!")
        return process, None

# Function to start all ngrok tunnels in parallel
def start_all_tunnels(tunnels):
    processes = []
    urls = {}

    for service_name, details in tunnels.items():
        process, port = start_tunnel(service_name, details['protocol'], details['port'])
        if port!=None:
            processes.append(process)
            urls[service_name] = f"{details['protocol']}://{BORE_BASE_URL}:{port}"
        else:
            graceful_shutdown(processes)
            sys.exit()

    return processes, urls

meta_processes = []

if LAB_NUM ==6:
    #Expose docker sock over TCP
    if sys.platform in ["darwin", "linux"]:
        print("[*nix] Using socat to forward tcp://localhost:2375 -> /var/run/docker.sock")
        socat_process = subprocess.Popen(["socat", "TCP-LISTEN:2375,reuseaddr,fork", "UNIX-CONNECT:/var/run/docker.sock"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
        meta_processes.append(socat_process)

if LAB_NUM ==7:
    #Expose k8s API
    k8s_api_port = "23112"
    command = ["kubectl", "proxy", "--address", "0.0.0.0", "--port", k8s_api_port, "--accept-hosts", ".*"]
    proxy_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
    meta_processes.append(proxy_process)

processes, urls = start_all_tunnels(tunnels)
processes.extend(meta_processes)

post_body = dict({"srn": SRN}, **urls)
# print(post_body)

print()

start_resp = requests.post(f"{BASE_URL}/lab/{LAB_NUM}/start", data=json.dumps(post_body), headers={"Content-Type": "application/json"})
if start_resp.status_code != 200:
    print("Something went wrong getting /start. Please contact a TA!")
    print(f"Status Code: {start_resp.status_code}, Response Body: {str(start_resp.content)}")
    graceful_shutdown(processes)
    sys.exit()

start_resp_json = start_resp.json()
message = start_resp_json["message"]
next_step = start_resp_json["next_step"]

while next_step!=-1:
    input(f"Step {next_step}> {message}. Hit ENTER when you are done.")

    print("Checking... ", end="", flush=True)
    next_step_resp = requests.post(f"{BASE_URL}/lab/{LAB_NUM}/step/{next_step}/check", data=json.dumps(post_body), headers={"Content-Type": "application/json"})
    if next_step_resp.status_code != 200:
        print(f"Something went wrong checking step {next_step}. Please contact a TA!")
        print(f"Status Code: {next_step_resp.status_code}, Response Body: {str(next_step_resp.content)}")

        if "connect:" in str(next_step_resp.content) or "read tcp" in str(next_step_resp.content):
            print("\nThere seems to be a problem connecting to Kubernetes, Are you sure you minikube is running?")

        print("This might be a spurious error so try restarting the marauders.py script. Do not worry, your progress will have been saved and the script will resume from the pending step")
        graceful_shutdown(processes)
        sys.exit()

    # try:
    #     next_step_resp_json = next_step_resp.json()
    # except json.decoder.JSONDecodeError:
    #     print("JSON Decode Error. Content:", next_step_resp.content)
    #     graceful_shutdown(processes)
    #     sys.exit()

    next_step_resp_json = next_step_resp.json()
    status = next_step_resp_json["status"]
    if status == "CHECKFAILED":
        err_message = next_step_resp_json["message"]
        print(f"Check Failed: {err_message}")
    elif status == "Success!":
        print("Check Successful! Step is complete")
        message = next_step_resp_json["message"]
        next_step = next_step_resp_json["next_step"]
    else:
        print(f"Something went wrong parsing check response for Step {next_step}. Please contact a TA!")
        print(f"Status Received: {status}")

        sys.exit()
    print()

print("Lab is Complete, Thank you!")
graceful_shutdown(processes)
print("Bye!")


