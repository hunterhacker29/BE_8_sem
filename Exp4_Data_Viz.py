# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Simple static dataset
# df = pd.DataFrame({
#     "math": [60, 70, 80, 90, 75],
#     "science": [65, 75, 85, 95, 70],
#     "english": [55, 65, 75, 85, 60],
#     "dept": ["A", "B", "A", "B", "A"]
# })

# # Univariate (single Variable)
# # Histogram
# plt.hist(df["math"], bins=3)
# plt.title("Math Histogram")
# plt.show()

# # Bar chart
# df["dept"].value_counts().plot(kind="bar")
# plt.title("Dept Count")
# plt.show()

# # Bivariate (two variables)
# # Scatter plot
# plt.scatter(df["math"], df["science"])
# plt.title("Math vs Science")
# plt.show()

# # Boxplot
# sns.boxplot(x="dept", y="math", data=df)
# plt.title("Math by Dept")
# plt.show()

# # Line chart
# plt.plot(df["math"])
# plt.plot(df["science"])
# # plt.legend()
# plt.title("Line Chart")
# plt.show()

# # Multivariate (simple pairplot)
# sns.pairplot(df)
# plt.show()






import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.DataFrame({
    
    
    "Math":[60, 70, 80, 90, 75],
    "Science":[65, 75, 85, 95, 70],
    "English":[55, 65, 75, 85, 60],
    "Dept":["A", "B", "A", "B", "A"]
})


print(df)


# single var 


plt.hist(df["Math"],bins= 3)
plt.show()


sns.boxplot(df["Math"])
plt.show()


# 2 var 

plt.scatter(df["Math"],df["English"])
plt.show()


# sns.hist(x = "Math", y = "Science", data = df)
# plt.show()


sns.boxplot(x = "Dept", y = "Math", data = df)
plt.show()


plt.plot(df["Math"])
plt.plot(df["Science"])
plt.show()


# var 

sns.pairplot(df)
plt.show()