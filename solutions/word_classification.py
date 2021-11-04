#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines = list(map(lambda s: s.rstrip(), data.readlines()))
    return lines

def get_features(a):
    col_num = len(alphabet_set)
    X = np.zeros(len(a) * col_num).reshape(len(a), col_num)
    for i, word in enumerate(a):
        X[i] = [word.count(letter) for letter in alphabet]
    return X

def contains_valid_chars(s):
    flag = np.sum([alphabet.count(i) for i in set(s)])==len(set(s))
    return flag

def get_features_and_labels():
    ## load finnish words:
    finn_data = load_finnish()
    new_finn_data = []
    for word in finn_data:
        word_lower = word.lower()
        if contains_valid_chars(word_lower) == True:
            new_finn_data.append(word_lower)

    ## load english words
    eng_data = load_english()
    new_eng_data = []
    for word in eng_data:
        if word[0].islower():
            word_lower = word.lower()
            if contains_valid_chars(word_lower) == True:
                new_eng_data.append(word_lower)
    data = new_finn_data + new_eng_data
    X = get_features(data)
    y = np.array([0] * len(new_finn_data) + [1] *len(new_eng_data))
    return X, y

def word_classification():
    X,y = get_features_and_labels()
    model = MultinomialNB()
    k_fold = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
    cross_val_score(model, X, y, cv=k_fold)
    return cross_val_score(model, X, y, cv=k_fold)

def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
