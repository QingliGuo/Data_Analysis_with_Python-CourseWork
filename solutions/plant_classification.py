#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

def plant_classification():
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size = 0.2, random_state = 0)
    model = GaussianNB()
    model.fit (X_train, y_train)
    y_test_fitted = model.predict(X_test)
    acc = accuracy_score(y_test, y_test_fitted)
    return acc

def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()
