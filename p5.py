import numpy as np
import pandas as pd

df = pd.read_csv("C:/Users/utsav/OneDrive/Desktop/data.csv")

d1 = df.columns
print(d1)

d2 = pd.read_csv("C:/Users/utsav/OneDrive/Desktop/data.csv",sep =",",header = "infer")
print(d2)

print(df.shape, df.dtypes, df.index, df.columns, sep ='\n-------------------\n')

print(df.head()) # Displays first 5 elements
print(df.tail()) # Dsiplays last 5 elements
print(df.info()) # Displays entire data set

print(df.head(2)) # Displays first 2 elements 

print(df.Pulse.head(3)) # Display specified column elements
print(df['Pulse'].head(5)) # Or optional

print(df[['Pulse']].head(5)) # Display specified column elements in good format
print(df[['Duration','Pulse']].head(7)) # Display multiple column elements
 
print(df.isna().any()) # Is there any missing value

print(df.isnull().sum()) # Count no of mising value

print(df[2:6]) # Slicing

print(df.iloc[[0]]) # Details of first row
print(df.iloc[[0,6]]) # Details of first row and 6 row
print(df.iloc[[70]]) # Details of 70 row
print(df.iloc[6].Pulse) # Details 6 row for pulse

print(df.iloc[2:9:2 , 2:5:2]) # Slicing in rows and columns

print(df.iloc[[2,3,4],[1,2,3]]) # Rows and columns location

# loc is location and iloc is index location
# loc takes names 
# iloc takes index values numbers

print(df.loc[[155]]) # Display label name with row
print(df.loc[[2,3,4],['Duration','Calories']]) # Rows and columns location

print(df.rename({'Duration':'Time'}, axis = 1)) # Change column name
# Axis = 1 means row wise
# Axis = 0 means column wise

print(df[df.Pulse == 110].head(3)) # Find similar range for column value

print(df.Pulse.unique()) # Unique category in column
print(df.Pulse.nunique()) # Number of unique categorie in column
print(df.Pulse.value_counts()) # Each category count

data = pd.concat([df[:3],df[:2]], ignore_index = True) # Create duplicate
data2 = data.drop_duplicates(inplace = True) # Deleting duplicates

