import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

#load our dataframe
df = pd.read_csv("dataFrame.csv")
pennData = pd.DataFrame(df)

print("-_"*20)
print("head of the data frame") #first five rows
print(pennData.head())

print("-_"*20)
print("tail of the data frame")
print(pennData.tail())

print("-_"*20)
print("summary of the data frame") 
print(pennData.info())

print("-_"*20)
print("stats of the data frame") 
print(round(pennData.describe()))

print("-_"*20)
print("head of the data frame")
print(pennData.head())

print("-_"*20)
print("count of students in pathways") 
print(pennData['pathway'].value_counts())

print("-_"*20)
print("avg gpa per year") 
print(pennData.groupby('year')['gpa'].mean())

print("-_"*20)
print("top 3 students by gpa") 
print(pennData.sort_values(by="gpa", ascending=False).head(3))

print("-_"*20)
print("student with gpa greater than 3.5") 
print(pennData[pennData['gpa']>3.5])

print("-_"*20)
print("first student data") 
print(pennData.iloc[0])

