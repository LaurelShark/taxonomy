from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, cophenet
from scipy.spatial.distance import pdist
import importlib
import numpy as np

np.random.seed(7455)
a = np.random.multivariate_normal([10, 0], [[3, 1], [1, 4]], [100, ])
print(a)
b = np.random.multivariate_normal([0, 20], [[3, 1], [1, 4]], [50, ])
X = np.concatenate((a, b), )
print(X.shape)
plt.scatter(X[:, 0], X[:, 1])
Z = linkage(X, 'single')
c, coph_dist = cophenet(Z, pdist(X))
# print(c)
# print(Z[1])
plt.figure(figsize=(25, 10))
plt.title('Hierachical Clustering Dendrogram')
plt.xlabel('sample matrix')
plt.ylabel('distance')
dendrogram(Z,
           truncate_mode='lastp',
           p=12,
           show_leaf_counts=True,
           leaf_rotation=90.,
           leaf_font_size=8,
           show_contracted=True, )
plt.show()
