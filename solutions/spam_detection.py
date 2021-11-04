#!/usr/bin/env python3
import gzip
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np

def spam_detection(random_state=0, fraction=0.1):
    spam_data = []
    with gzip.open("./src/spam.txt.gz", "rt") as f:
        for line in f:
            spam_data.append(line)

    ham_data = []
    with gzip.open("./src/ham.txt.gz", "rt") as f:
        for line  in f:
            ham_data.append(line)
    ## Take the fraction of data forward:
    spam_data = spam_data[:np.int(fraction * len(spam_data))]
    ham_data = ham_data[:np.int(fraction * len(ham_data))]
    
    vec=CountVectorizer()
    X = vec.fit_transform(ham_data + spam_data)
    y = np.array([0] * len(ham_data) + [1] * len(spam_data))
    X_train, X_test, y_train, y_test = train_test_split (X, y, test_size = 0.25, random_state = random_state)
    
    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_test_fitted = model.predict(X_test)
    
    acc = accuracy_score(y_test_fitted, y_test)
    test_sample_size = X_test.shape[0]
    mis_classified = np.int((1 - acc) * test_sample_size)
    
    return acc, test_sample_size, mis_classified

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
