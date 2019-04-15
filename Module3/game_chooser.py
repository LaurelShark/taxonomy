import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

programs = [[0, 11, 2.1, 1.1, 1.1],
            [1, 0, 0.9, 0.1, 0.1]]

labels = ['poroshenko', 'zelenskii', 'you']

positions = ['referendym_nato']

your_vector = []
num_1 = int(input("Do you agree that with holding "
                  "a referendum for membership in NATO? (1 - yes, 0 - no)"))
your_vector.append(num_1)
num_2 = int(input("How much you agree that diplomatic way is "
                  "the most acceptable way to return Donbass and Crimea? "
                  "(10 - agree, 1 - strongly disagree)"))
your_vector.append(num_2)
num_3 = int(input("What is more important for you:"
                  "1 - free annual medical review; "
                  "2 - increasing the amount of birth aid and for"
                  "low income families?"))
your_vector.append(num_3)
num_4 = int(input("Do you agree that the taxation of corporate profits "
                  "has to be changed to taxation of capital withdrawal from the country" 
                  "(1 - yes, 0 - no)"))
your_vector.append(num_4)
num_5 = int(input("Is political experience obligatory for president of your country?"
                  "(1 - yes, 0 - no)"))
your_vector.append(num_5)

programs.append(your_vector)

Z = linkage(programs, 'ward')
plt.figure(figsize=(50, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('This is how close is you to election candidates')
plt.ylabel('distance')
dendrogram(
    Z,
    labels=labels,
    leaf_rotation=90.,
    leaf_font_size=10,
)
plt.gcf().subplots_adjust(bottom=0.20)
plt.show()
