



import pandas as pd

df = pd.DataFrame(
      
      {
            "Name":["Alice", "Bob", "Charlie", "David", "Eve", None ],
            "Age":[25, 30, 30 , 40, 45, None],
            "Marks":[75, 30, 75, None, 75, None],
      
      }      
) 


print(df)

print(df.info())


print(df.isnull().sum())

df ['Name']=df["Name"].fillna("Unknown")
print(df)

df ['Age']=df["Age"].fillna(df["Age"].mean())
print(df)

df ['Marks']=df["Marks"].fillna(df["Marks"].median())
print(df)


print("-----------------------------------")
print(df.duplicated().sum())



df = df.drop_duplicates()
print(df)

df = df.dropna()
print(df)