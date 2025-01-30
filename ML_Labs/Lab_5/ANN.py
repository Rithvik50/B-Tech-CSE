import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Load and preprocess the data
# input: filepath: str (path to the CSV file)
# output: tuple of X (features), y (target)
def load_and_preprocess_data(filepath):
    data = pd.read_csv(filepath)
    data = data.drop(columns = ['GarbageValues'])
    data = data.dropna()

    target_col = "Outcome"
    X = data.drop(columns = [target_col])
    y = data[target_col]

    return X, y

# Split the data into training and testing sets
# input: 1) X: ndarray (features)
#        2) y: ndarray (target)
# output: tuple of X_train, X_test, y_train, y_test
def split_and_standardize(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.5, random_state = 50)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test

# Create and train 2 MLP classifiers with different parameters
# input:  1) X_train: ndarray
#         2) y_train: ndarray
# output: tuple of models (model1, model2)
def create_model(X_train, y_train):
    model1 = MLPClassifier(hidden_layer_sizes = (60, 50, 10), activation = 'relu', max_iter = 100, random_state = 60)
    model2 = MLPClassifier(hidden_layer_sizes = (40, 20, 30), activation = 'tanh', max_iter = 200, random_state = 30)

    model1.fit(X_train, y_train)
    model2.fit(X_train, y_train)

    return model1, model2

# Predict and evaluate the model
# input: 1) model: MLPClassifier after training
#        2) X_test: ndarray
#        3) y_test: ndarray
# output: tuple - accuracy, precision, recall, fscore, confusion_matrix
def predict_and_evaluate(model, X_test, y_test):
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average = 'weighted')
    recall = recall_score(y_test, y_pred, average = 'weighted')
    f1score = f1_score(y_test, y_pred, average = 'weighted')
    conf_matrix = confusion_matrix(y_test, y_pred)

    return accuracy, precision, recall, f1score, conf_matrix
