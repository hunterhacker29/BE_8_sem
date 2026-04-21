

import matplotlib.pyplot as plt 
import seaborn as sns 

import pandas as pd

df = pd.read_csv("Dataset\\instaData.csv")
print(df)


print(df.columns)

# print(df['Likes'])


# Drawing Pie chart platform 
plat = df["Platform"].value_counts()
print(plat)


plat.plot.pie()
plt.title("Platform Distribution")
plt.show()


plt.bar(df['User'],df['Likes'])
plt.title("Likes Per post")
plt.xlabel("User")
plt.ylabel("Likes")
plt.show()


plt.plot(df['Likes'])
plt.title("Likes Trend")
plt.show()


sns.countplot(x="Platform",data = df )
plt.show()


plt.hist(df["Likes"])
plt.show()

plt.scatter(df["Likes"],df["Comments"])
plt.show()

plt.boxplot(df["Likes"])
plt.show()

