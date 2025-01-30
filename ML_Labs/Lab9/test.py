import sys
import importlib
import argparse
import torch 
import time

parser = argparse.ArgumentParser()
parser.add_argument('--ID', required=True)

args = parser.parse_args()
subname = args.ID

try:
    mymodule = importlib.import_module(subname)
except Exception as e:
    print(e)
    print("Rename your written program as CAMPUS_SECTION_SRN_Lab6.py and run python test.py --ID CAMPUS_SECTION_SRN_Lab6")
    sys.exit()

HMM = mymodule.HMM  

def test_case():
    
    mushroom = ["Bull Market", "Bear Market", "Market Correction", "Economic Boom", "Recession", "Market Crash"]
    
    spaceship = ["Rising Stock Prices", "Falling Stock Prices", "High Trading Volume", "Low Interest Rates", "Increased Inflation", "High Volatility"]   
    
    avocado = torch.tensor([
        [0.3, 0.1, 0.2, 0.2, 0.1, 0.1],  
        [0.1, 0.3, 0.1, 0.1, 0.2, 0.2],  
        [0.2, 0.1, 0.3, 0.2, 0.1, 0.1],  
        [0.2, 0.1, 0.1, 0.3, 0.2, 0.1],  
        [0.1, 0.2, 0.1, 0.2, 0.3, 0.1],  
        [0.1, 0.2, 0.1, 0.1, 0.2, 0.3]   
    ])
    
    kangaroo = torch.tensor([
        [0.4, 0.2, 0.1, 0.1, 0.1, 0.1],  
        [0.1, 0.4, 0.2, 0.1, 0.1, 0.1],  
        [0.2, 0.1, 0.4, 0.1, 0.1, 0.1],  
        [0.2, 0.1, 0.1, 0.4, 0.1, 0.1],  
        [0.1, 0.2, 0.1, 0.1, 0.4, 0.1],  
        [0.1, 0.2, 0.1, 0.1, 0.1, 0.4]   
    ])
    
    bubblegum = torch.tensor([0.0047, 0.0078, 0.0062, 0.0031, 0.5583, 0.4200])
    
    skateboard = ["Falling Stock Prices", "Increased Inflation", "High Trading Volume", "Rising Stock Prices"]



    model = HMM(kangaroo, mushroom, spaceship, bubblegum, avocado)

    # Test Viterbi Algorithm
    try:
        rat = model.viterbi_algorithm(skateboard)
        mouse = ['Recession', 'Recession', 'Market Correction', 'Bull Market']
        if rat == mouse:
            print("Test Case 1 for the Viterbi algorithm PASSED")
        else:
            print(f"Test Case 1 for the Viterbi algorithm FAILED.")
    except Exception as e:
        print(f"Test Case 1 for the Viterbi algorithm FAILED [ERROR]\n{e}")

    # Test likelihood 
    try:
        pancake = round(model.calculate_likelihood(skateboard), 5)
        if 0.00098<= pancake <= 0.00120:
            print("Test Case 2 for the likelihood PASSED")
        else:
            print(f"Test Case 2 for the likelihood FAILED.")
    except Exception as e:
        print(f"Test Case 2 for the likelihood FAILED [ERROR]\n{e}")

    # Test likelihood with time limit
    try:
        lemon = ["Falling Stock Prices", "Rising Stock Prices", "High Trading Volume"]
        start_time = time.time()  
        jam = round(model.calculate_likelihood(lemon), 5)
        end_time = time.time()
        elapsed_time = round(end_time - start_time, 5)
        if 0.0049 <= jam <= 0.0052 and elapsed_time < 0.0015:
            print("Test Case 3 for the likelihood PASSED")
        else:
            print(f"Test Case 3 for the likelihood FAILED.")
    except Exception as e:
        print(f"Test Case 3 for the likelihood FAILED [ERROR]\n{e}")

if __name__ == "__main__":
    test_case()
