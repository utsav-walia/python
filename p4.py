import pandas as pd

ser = pd.Series(["Utsav","Trainer",3,"Mech Engg"],["Name","Designation","Exp","Qualification"])
print(ser) # Displays Series

d = ({'A':1,'B':2,'C':3}) # Dictionary Display
s = pd.Series(d)
print(s)

print(ser["Name"]) # Displays Particular element from the series

df = pd.DataFrame({'Name' :["Nimish","Rahul"], 'Age' : [32,28]})
print(df) # Displays arranged form of data rows and columns

df2 = pd.DataFrame(ser)
print(df2) # Displays series into data frame
