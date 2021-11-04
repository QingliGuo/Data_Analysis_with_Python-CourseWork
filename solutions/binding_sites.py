#!/usr/bin/env python3
import scipy
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

def toint(x):
    dic = {'A':0, "C":1, "G":2, "T":3}
    if len(x) == 1:
        return [dic[letter] for letter in x][0]
    else:
        return [dic[letter] for letter in x]

def get_features_and_labels(filename = "./src/data.seq"):
    df = pd.read_csv(filename, sep = "\t")
    X = np.zeros (df.shape[0] * 8).reshape(df.shape[0], 8)
    for i, seq in enumerate(df['X'].values):
        X[i] = toint(seq)
    y = df['y'].to_numpy()
    return (X.astype(int), y)

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def cluster_euclidean(filename = "./src/data.seq"):
    X,y = get_features_and_labels()
    cluster = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='average')
    y_fitted = cluster.fit_predict(X)
    permutation = find_permutation(n_clusters = 2, real_labels = y, labels = y_fitted)
    new_labels = [permutation[label] for label in y_fitted]
    return accuracy_score(new_labels, y)

def cluster_hamming(filename = "./src/data.seq"):
    X,y = get_features_and_labels()
    D = pairwise_distances(X, metric='hamming')
    cluster = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage = 'average')
    y_fitted = cluster.fit_predict(D)
    permutation = find_permutation(n_clusters = 2, real_labels = y, labels = y_fitted)
    new_labels = [permutation[label] for label in y_fitted]
    
    return accuracy_score(new_labels, y)

def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()
