from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
import numpy as np
import random
from pprint import pprint


def get_optimal_k(data, kmin, kmax, splits):
    optimal_s = 0
    optimal_k = kmin
    ks = [kmin, kmax]
    ks_unsorted = [kmin, kmax]

    for _ in range(0, splits):
        ks.sort()
        for i in range(0, len(ks) - 1):
            v = int((ks[i] + ks[i + 1]) / 2)
            ks.append(v)
            ks_unsorted.append(v)

    for k in list(set(ks)):
        kmeans = KMeans(n_clusters=k).fit(data)
        s = silhouette_score(data, kmeans.labels_, metric="euclidean")
        print(f"silhouette score for k = {k} is {s}")
        if s > optimal_s:
            optimal_s = s
            optimal_k = k

    print(f"optimal k is {optimal_k}")
    return optimal_k


def clusterize(data, k=10):
    kmeans = KMeans(
        init="random",
        n_clusters=k,
        max_iter=500,
        random_state=42
    )

    kmeans.fit(data)

    return list(zip(
        np.array(kmeans.labels_).astype('str').tolist(),
        data,
    ))
