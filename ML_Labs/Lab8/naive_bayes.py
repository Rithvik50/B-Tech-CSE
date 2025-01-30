import numpy as np
import warnings
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

warnings.filterwarnings("ignore", category = RuntimeWarning)

class NaiveBayesClassifier:
    """
    A simple implementation of the Naive Bayes Classifier for text classification.
    """

    @staticmethod
    def preprocess(sentences, categories):
        """
        Preprocess the dataset to remove stop words, and missing or incorrect labels.

        Args:
            sentences (list): List of sentences to be processed.
            categories (list): List of corresponding labels.

        Returns:
            tuple: A tuple of two lists - (cleaned_sentences, cleaned_categories).
        """
        cleaned_sentences = []
        cleaned_categories = []

        for sentence, category in zip(sentences, categories):
            if category and category not in ["None", "wrong_label"]:
                words = sentence.split()
                filtered_sentence = ' '.join(word for word in words if word.lower() not in ENGLISH_STOP_WORDS)
                cleaned_sentences.append(filtered_sentence)
                cleaned_categories.append(category)

        return cleaned_sentences, cleaned_categories

    @staticmethod
    def fit(X, y):
        """
        Trains the Naive Bayes Classifier using the provided training data.
        
        Args:
            X (numpy.ndarray): The training data matrix where each row represents a document
                              and each column represents the presence (1) or absence (0) of a word.
            y (numpy.ndarray): The corresponding labels for the training documents.

        Returns:
            tuple: A tuple containing two dictionaries:
                - class_probs (dict): Prior probabilities of each class in the training set.
                - word_probs (dict): Conditional probabilities of words given each class.
        """
        class_probs = {}
        word_probs = {}
        total_docs = len(y)

        unique_classes, counts = np.unique(y, return_counts=True)
        for cls, count in zip(unique_classes, counts):
            class_probs[cls] = count / total_docs

        word_count_per_class = {cls: np.zeros(X.shape[1]) for cls in unique_classes}
        total_words_per_class = {cls: 0 for cls in unique_classes}

        for i in range(total_docs):
            cls = y[i]
            word_count_per_class[cls] += X[i]
            total_words_per_class[cls] += np.sum(X[i])

        for cls in unique_classes:
            word_probs[cls] = (word_count_per_class[cls] + 1) / (total_words_per_class[cls] + len(unique_classes))

        return class_probs, word_probs

    @staticmethod
    def predict(X, class_probs, word_probs, classes):
        """
        Predicts the classes for the given test data using the trained classifier.

        Args:
            X (numpy.ndarray): The test data matrix where each row represents a document
                              and each column represents the presence (1) or absence (0) of a word.
            class_probs (dict): Prior probabilities of each class obtained from the training phase.
            word_probs (dict): Conditional probabilities of words given each class obtained from training.
            classes (numpy.ndarray): The unique classes in the dataset.

        Returns:
            list: A list of predicted class labels for the test documents.
        """
        predictions = []

        for x in X:
            max_prob = -np.inf
            best_class = None

            for cls in classes:
                log_prob = np.log(class_probs[cls])

                for idx, word_presence in enumerate(x):
                    if word_presence > 0:
                        log_prob += np.log(word_probs[cls][idx])
                    else:
                        log_prob += np.log(1 - word_probs[cls][idx])

                if log_prob > max_prob:
                    max_prob = log_prob
                    best_class = cls

            predictions.append(best_class)

        return predictions
