

import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

value = np.array([[2,2],[2.1,2.1],[4,4],[5,5],[6,6.5], [4.5,5]])
plt.scatter(value[:,0], value[:,1], s=50)

linkage_matrix = linkage(value, "ward")
dendogram = dendrogram(linkage_matrix, truncate_mode='none')
plt.title("Hierarchical clustering")
plt.show()

