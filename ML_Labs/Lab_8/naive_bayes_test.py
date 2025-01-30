from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from naive_bayes import NaiveBayesClassifier
import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)

def run_tests(test_cases):
    # Defining the training sentences and categories
    sentences = [
        "I can't wait to visit the pyramids in Egypt.",  # Travel
        "Regular exercise is vital for a healthy life.",  # Health
        "Reading classic literature expands your horizons.",  # Literature
        "Exploring the fjords of Norway was a dream come true.",  # Travel
        "A balanced diet can improve your immune system.",  # Health
        "The novel I read last month was a real page-turner.",  # Literature
        "Traveling to new places broadens your perspective.",  # Travel
        "Meditation can reduce stress and enhance well-being.",  # Health
        "Shakespeare's plays are still relevant today.",  # Literature
        "Hiking in the mountains is a great way to unwind.",  # Travel
        "Eating fruits and vegetables is important for health.",  # Health
        "The poem I wrote won an award.",  # Literature
        "Missing label",  # Missing label (noise)
        "Incorrect label"  # Incorrect label (noise)
    ]

    categories = [
        "travel", "health", "literature", "travel", "health", "literature", "travel",
        "health", "literature", None, "health", "literature", None, "wrong_label"
    ]

    # Preprocessing step
    sentences, categories = NaiveBayesClassifier.preprocess(sentences, categories)

    # Vectorizing the text data using CountVectorizer
    vectorizer = CountVectorizer()
    X_train_vec = vectorizer.fit_transform(sentences)

    # Fitting the Naive Bayes model
    class_probs, word_probs = NaiveBayesClassifier.fit(X_train_vec.toarray(), categories)

    num_passed = 0

    for test_sentence, correct_category in test_cases:
        test_vector = vectorizer.transform([test_sentence]).toarray()
        prediction = NaiveBayesClassifier.predict(test_vector, class_probs, word_probs, np.unique(categories))[0]

        if prediction == correct_category:
            print(f"Test Passed: '{test_sentence}' - Predicted: {prediction} | Correct: {correct_category}")
            num_passed += 1
        else:
            print(f"Test Failed: '{test_sentence}' - Predicted: {prediction} | Correct: {correct_category}")

    return num_passed


if __name__ == "__main__":
    test_cases = [
        ("Traveling to Japan is on my bucket list.", "travel"),
        ("Yoga greatly improves mental clarity.", "health"),
        ("The Great Gatsby is a must-read for everyone.", "literature"),
        ("Traveling allows for the discovery of diverse cultures and breathtaking landscapes.", "travel"),
        ("Regular check-ups can catch health issues early.", "health"),
        ("This novel delves into the complexities of human relationships.", "literature"),
        ("Exploring the Amazon rainforest was an adventure of a lifetime.", "travel"),
        ("Nutrition plays a crucial role in our well-being.", "health"),
        ("The novel's intricate plot twists kept me on the edge of my seat until the very last page.", "literature"),
        ("I dream of sailing through the Greek islands.", "travel")
    ]

    num_passed = run_tests(test_cases)
    print(f"\nNumber of Test Cases Passed: {num_passed} out of {len(test_cases)}")
