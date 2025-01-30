import sys
import importlib
import argparse
import warnings

warnings.filterwarnings("ignore")
parser = argparse.ArgumentParser()
parser.add_argument("--ID", required=True)
parser.add_argument("--data",required=True)
parser.add_argument("--test",required=True)
args = parser.parse_args()
subname = args.ID
train_path = args.data
test_path = args.test
try:
    mymodule = importlib.import_module(subname)
except Exception as e:
    print(e)
    print("Rename your program to SRN.py and run `python Test.py --ID SRN`.")
    sys.exit()

prepareData = mymodule.prepareData
CNN = mymodule.CNN
train = mymodule.train
evaluate = mymodule.evaluate

def test_case():
    train_loader, test_loader = prepareData(train_path,test_path)
    model = CNN()
    print(model)
    # Train the model
    train_accuracy = train(model, train_loader)

    # Evaluate the model
    test_accuracy = evaluate(model, test_loader)

    if train_accuracy >= 92:
        print("Test Case 1 for train PASSED")
    else:
        print("Test Case 1 for train FAILED")
    
    if test_accuracy >= 87:
        print("Test Case 2 for evaluate PASSED")
    else:
        print("Test Case 2 for evaluate FAILED")
        
    if test_accuracy >= 90:
        print("Test Case 3 for evaluate PASSED")
    else:
        print("Test Case 3 for evaluate FAILED")

if __name__ == "__main__":
    test_case()
