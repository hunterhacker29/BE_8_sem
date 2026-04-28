
# Using Distance based 

 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.neighbors import NearestNeighbors


data = [1,2,3,4,2,2,1,4,100]
x = np.array(data).reshape(-1,1)


model = NearestNeighbors(n_neighbors=2)
model.fit(x)

d  = model.kneighbors(x)
print("Distances to nearest neighbors: ", d)

plt.scatter (range(len(data)), data)
plt.show()



### using box plot


import matplotlib.pyplot as plt

data = [1,2,3,4,2,2,1,4,100]

# Boxplot
plt.boxplot(data)
plt.title("Boxplot with Outliers")
plt.show()