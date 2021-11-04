#!/usr/bin/env python3

import scipy
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def plant_clustering():
    data = load_iris()
    n_cluster = 3
    model = KMeans(n_clusters = n_cluster, random_state=0)
    model.fit(data.data)
    permutation = find_permutation(n_cluster, data.target, model.labels_)
    new_labels = [permutation[label] for label in model.labels_]   # permute the labels
    return accuracy_score(data.target, new_labels)

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()
