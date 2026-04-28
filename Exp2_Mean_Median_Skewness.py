import pandas as pd
import numpy as np
from scipy.stats import kurtosis , skew 
import matplotlib.pyplot as plt 



data = [2,3,3,3,4,4,4,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,7,7,7,7,8,9,10]

# print(df)
df= np.array(data)
print(df)


print(f"Mean:{np.mean(df)}")
print(f"Median:{np.median(df)}")
print(f"kurtosis:{kurtosis(df)}")
print(f"skewness:{skew(df)}")


plt.hist(data,bins=range(2,12))
plt.show()


