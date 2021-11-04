#!/usr/bin/env python3
import scipy
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def nonconvex_clusters():
    df = pd.read_csv("./src/data.tsv", sep = "\t")

    X = df.iloc[:,:2].to_numpy()
    y = df.iloc[:,2].to_numpy()

    epss = np.arange(0.05, 0.2, 0.05)

    scores = []
    clusters = []
    outliers = []

    for eps in epss:
        model = DBSCAN(eps = eps)
        model.fit(X)
    
        nonoutlier_idx = model.labels_ != -1
        outlier_idx = model.labels_ == -1

        num_clusters = len(set(model.labels_[nonoutlier_idx]))
        num_outliers = np.sum(outlier_idx)
        if num_clusters == len(set(y)):
            permutation = find_permutation(num_clusters, model.labels_, y)
            new_labels = [permutation[label] for label in model.labels_[nonoutlier_idx]]   # permute the labels
            acc = accuracy_score(new_labels, y[nonoutlier_idx])
        else:
            acc = np.NaN
        scores.append(acc)
        clusters.append(num_clusters)
        outliers.append(num_outliers)
    output = pd.DataFrame({"eps":list(epss), "Score":scores, "Clusters": clusters, "Outliers":outliers})
    output = output.astype("float64")
    return output


def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
