

import re 
import pandas as pd 


df = pd.read_csv("Dataset\\social_media_raw.csv")
print(df)


print("Data INfo ")

df.info()
print(df.describe())

print("Null values in data set ")
print(df.isnull())
print(df.isnull().sum())

print("Dropping null values and replacing it ")
df["Post_Text"]=df["Post_Text"].fillna("No text")
print(df)


print("checking for duplicate ")

print(df.duplicated())
print(df.duplicated().sum())

print("Dropping Duplicate")
df.drop_duplicates(inplace=True)


df["Post_Text"]=df["Post_Text"].str.replace(r'[^\w\s]', '',regex=True)
print(df)