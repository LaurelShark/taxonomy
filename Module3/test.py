import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

df = pd.read_csv("candidates_data.csv")
labels = np.array(df['last_name'])
df = df.iloc[:, 1:15]
df.head()

Z = linkage(df, 'ward')
plt.figure(figsize=(50, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Election candidates, Ukraine 2019')
plt.ylabel('distance')
dendrogram(
    Z,
    labels=labels,
    leaf_rotation=90.,
    leaf_font_size=10,
)
plt.gcf().subplots_adjust(bottom=0.20)
plt.show()
