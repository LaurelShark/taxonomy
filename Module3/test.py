import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt


df = pd.read_csv("heart.csv")
df = df.iloc[:, 0:14]

df.head()
Z = linkage(df, 'single')
plt.figure(figsize=(50, 10))
plt.title('Heart disease clustering diagram')
plt.xlabel('heart disease dataset')
plt.ylabel('distance')
dendrogram(Z,
           leaf_rotation=90.,
           leaf_font_size=8,
           )
plt.show()
