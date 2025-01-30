import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from torch.utils.data import DataLoader, TensorDataset

# Dataset Preparation
def prepareData(train_path,test_path):
    data_raw = pd.read_csv(train_path, sep=",")
    test_data_raw = pd.read_csv(test_path, sep=",")
    
    labels = data_raw['label']
    data_raw.drop('label', axis=1, inplace=True)
    
    labels_test = test_data_raw['label']
    test_data_raw.drop('label', axis=1, inplace=True)
    
    # Normalize data and map labels
    data = data_raw.values / 255.0
    labels = labels.values
    test_data = test_data_raw.values / 255.0
    labels_test = labels_test.values
    
    # Remap labels: J is excluded, so labels >= 9 should be reduced by 1
    labels[labels >= 9] -= 1
    labels_test[labels_test >= 9] -= 1

    # Convert to tensors and create data loaders
    train_dataset = TensorDataset(torch.tensor(data, dtype=torch.float32).reshape(-1, 1, 28, 28),
                                  torch.tensor(labels, dtype=torch.long))
    test_dataset = TensorDataset(torch.tensor(test_data, dtype=torch.float32).reshape(-1, 1, 28, 28),
                                 torch.tensor(labels_test, dtype=torch.long))
    
    train_loader = DataLoader(train_dataset, batch_size=100, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=100, shuffle=False)
    
    return train_loader, test_loader

# CNN Model
class CNN(nn.Module):
    def __init__(self):
        #TODO
        # ----------------------------------------------
        # TODO: Define the CNN layers (Conv layers, Pooling layers, Fully connected layers) 
        # and the  optimizer
        #----------------------------------------------------------------------------------
        super(CNN, self).__init__()
        # Define the CNN layers
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc1 = nn.Linear(128 * 3 * 3, 256)
        self.fc2 = nn.Linear(256, 24)  # 24 classes
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(p=0.5)  # Dropout to avoid overfitting


    def forward(self, x):
        # TO DO
        # ----------------------------------------------
        # TODO: Define the forward pass through the network.
        # Pass x through convolution layers, pooling layers, flatten, and fully connected layers.
        # ----------------------------------------------
        x = self.relu(self.conv1(x))
        x = self.pool(x)
        x = self.relu(self.conv2(x))
        x = self.pool(x)
        x = self.relu(self.conv3(x))
        x = self.pool(x)

        # Flatten the tensor
        x = x.view(x.size(0), -1)
        
        # Fully connected layers with dropout
        x = self.relu(self.fc1(x))
        x = self.dropout(x)  # Apply dropout after the first fully connected layer
        x = self.fc2(x)  # Output layer
        return x

# Training loop
def train(model, train_loader, epochs=6):
    #TODO
    # Return : Train Accuracy (float)
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.CrossEntropyLoss()

    for epoch in range(epochs):
        total_loss = 0
        correct = 0
        total = 0
        for inputs, labels in train_loader:
            
            optimizer.zero_grad()
            
            # Forward pass
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            
            # Backward pass and optimize
            loss.backward()
            optimizer.step()
            
            # Update running loss and correct predictions
            total_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            correct += (predicted == labels).sum().item()
            total += labels.size(0)
        
        accuracy = 100 * correct / total
        print(f'Epoch {epoch+1}, Loss: {total_loss:.4f}, Train Accuracy: {accuracy:.2f}%')

        # Intermediate evaluation after each epoch
        model.eval()  # Set model to evaluation mode
        test_correct = 0
        test_total = 0
        with torch.no_grad():
            for inputs, labels in train_loader:  # Use test_loader if provided
                outputs = model(inputs)
                _, predicted = torch.max(outputs, 1)
                test_correct += (predicted == labels).sum().item()
                test_total += labels.size(0)
        test_accuracy = 100 * test_correct / test_total
        print(f"Intermediate Test Accuracy at Epoch {epoch + 1}: {test_accuracy:.2f}%")
                
        accuracy = 100 * correct / total
        print(f'Epoch {epoch+1}, Loss: {total_loss:.4f}, Accuracy: {accuracy:.2f}%')
        
    return accuracy

# Evaluation loop
def evaluate(model, test_loader):
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in test_loader:
            outputs = model(inputs)
            _, predicted = torch.max(outputs, 1)
            correct += (predicted == labels).sum().item()
            total += labels.size(0)
    
    accuracy = 100 * correct / total
    print(f'Test Accuracy: {accuracy:.2f}%')
    return accuracy
