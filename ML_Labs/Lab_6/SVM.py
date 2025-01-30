import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC, SVR
from sklearn.metrics import accuracy_score, mean_absolute_percentage_error
import matplotlib.pyplot as plt

# SVM Classification Class
class SVM_Classification:
    def __init__(self) -> None:
        self.model = None

    def dataset_read(self, dataset_path):
        """
        Read the dataset from the JSON file and split it into features (X) and target (y).
        :param dataset_path: The file path to the dataset in JSON format.
        :return: Features (X) and target variable (y).
        """
        data = pd.read_json(dataset_path)
        X = data.drop(columns=['target'])
        y = data['target']
        return X, y

    def preprocess(self, X, y):
        """
        Handle missing values and standardize the features using StandardScaler.
        :param X: Features (input variables).
        :param y: Target (output variable).
        :return: Preprocessed features (X) and target (y).
        """
        X.fillna(X.median(), inplace=True)
        
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        return X_scaled, y

    def train_classification_model(self, X_train, y_train):
        """
        Initialize an SVC model and train it on the training data.
        :param X_train: Training set features.
        :param y_train: Training set labels.
        """
        self.model = SVC(kernel = 'sigmoid',random_state=0)
        self.model.fit(X_train, y_train)

    def predict_accuracy(self, X_test, y_test):
        """
        Predict the target values using the test data and calculate the accuracy score.
        :param X_test: Test set features.
        :param y_test: True target values.
        :return: Accuracy score.
        """
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        return accuracy

# SVM Regression Class
class SVM_Regression:
    def __init__(self) -> None:
        self.model = None

    def dataset_read(self, dataset_path):
        """
        Read the dataset from the JSON file and split it into features (X) and target (y).
        :param dataset_path: The file path to the dataset in JSON format.
        :return: Features (X) and target variable (y).
        """
        data = pd.read_json(dataset_path)
        X = data.drop(columns=['alcohol'])
        y = data['alcohol']
        return X, y

    def preprocess(self, X, y):
        """
        Handle missing values and standardize the features using StandardScaler.
        :param X: Features (input variables).
        :param y: Target (output variable).
        :return: Preprocessed features (X) and target (y).
        """
        X.fillna(X.median(), inplace=True)
        
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        return X_scaled, y

    def train_regression_model(self, X_train, y_train):
        """
        Initialize an SVR model and train it on the training data.
        :param X_train: Training set features.
        :param y_train: Training set target values.
        """
        self.model = SVR()
        self.model.fit(X_train, y_train)

    def predict_accuracy(self, X_test, y_test):
        """
        Predict the target values using the test data and calculate the mean absolute percentage error (MAPE).
        :param X_test: Test set features.
        :param y_test: True target values.
        :return: Accuracy score (1 - MAPE).
        """
        y_pred = self.model.predict(X_test)
        err = mean_absolute_percentage_error(y_test, y_pred)
        return 1 - err

    def visualize(self, X_test, y_test, y_pred):
        """
        Visualize the comparison between actual and predicted target values.
        :param X_test: Test set features.
        :param y_test: Actual target values.
        :param y_pred: Predicted target values.
        """
        plt.figure(figsize=(10, 6))
        plt.scatter(X_test, y_test, color='blue', alpha=0.6, edgecolor='k', label='Actual Target')
        plt.scatter(X_test, y_pred, color='red', alpha=0.6, edgecolor='k', label='Predicted Target')
        plt.title('X vs Target')
        plt.xlabel('X')
        plt.ylabel('Target')
        plt.legend()
        plt.grid(True)
        plt.show()

# SVM Spiral Classification Class
class SVM_Spiral:
    def __init__(self) -> None:
        self.model = None

    def dataset_read(self, dataset_path):
        """
        Read the dataset from the JSON file and split it into features (X) and target (y).
        :param dataset_path: The file path to the dataset in JSON format.
        :return: Features (X) and target variable (y).
        """
        data = pd.read_json(dataset_path)
        X = data.drop(columns=['targets'])
        y = data['targets']
        return X, y

    def preprocess(self, X, y):
        """
        Handle missing values and standardize the features using StandardScaler.
        :param X: Features (input variables).
        :param y: Target (output variable).
        :return: Preprocessed features (X) and target (y).
        """
        X.fillna(X.mean(), inplace=True)
        
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        return X_scaled, y

    def train_spiral_model(self, X_train, y_train):
        """
        Initialize an SVC model with a suitable kernel and train it on the training data.
        :param X_train: Training set features.
        :param y_train: Training set labels.
        """
        self.model = SVC(kernel = 'rbf', gamma = 19, C = 10)
        self.model.fit(X_train, y_train)

    def predict_accuracy(self, X_test, y_test):
        """
        Predict the target values using the test data and calculate the accuracy score.
        :param X_test: Test set features.
        :param y_test: True target values.
        :return: Accuracy score.
        """
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        return accuracy