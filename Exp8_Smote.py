
import pandas as pd 
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt
import numpy as np 

d = [1,2,3,4,2,2,100,101]
x = np.array(d).reshape(-1,1)
y = [0,0,0,0,0,0,1,1]


model = SMOTE(k_neighbors=1)
x_res , y_res = model.fit_resample(x,y)

print("Before SMOTE:", len(x))
print("After SMOTE:", len(x_res))

for i in range(len(x_res)):
    if y_res[i] == 0 :
        plt.scatter(i,x_res[i],marker = 'o')
        
    else :
        plt.scatter(i,x_res[i],marker = 'x')

plt.show()

