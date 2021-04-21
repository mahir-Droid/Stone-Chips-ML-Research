# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 21:32:35 2020

@author: soheb
"""

"""
a = {'a','b','c','d'}


s1 = "apple"

s2 = "orange"

s3 = "apple and orange is my favorite"

print(s1 in s3)
print( ('apple' in s3) or (s2 in s3))


for i in a:
    print(i)
    
    
data = {'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka'], 
                'Age': [21, 19, 20, 18], 
                'Stream': ['Math', 'Commerce', 'Arts', 'Biology'], 
                'Percentage': [88, 92, 95, 70]} 
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data, columns = ['Name', 'Age', 'Stream', 'Percentage'])

print(df)
'''
for i, j in enumerate(data['Name']):
    print(i,j)
    
for i in df.index: 
     print(i, 'a' in df['Name'][i])
'''

print(df['Name'].get(0))
print("......")
print("......")
print("......")
print("......")
print("......")

"""


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

dt = pd.read_excel('FinalDataClean.xlsx')


dt['Sample Location'] = dt['Sample Location'].astype(str)
dt['Construction Year'] = dt['Construction Year'].astype(str)
dt['Fracture Type'] = dt['Fracture Type'].astype(str)



# Cleaning for Sample Location
dropList = []

for i, j in enumerate(dt['Sample Location']):
    mixed = ( ('B' in j) and ('C' in j) ) or ( ('B' in j) and ('F' in j) ) or ( ('C' in j) and ('F' in j) ) or ( ('B' in j) and ('W' in j) )
    
    if(mixed):
        dropList.append(i)
    elif('B' in j):
        dt.loc[i,'Sample Location'] = 'B'
    elif('F' in j):
        dt.loc[i,'Sample Location'] = 'F'
    elif( ('Not available' in j) or ('Not Mentioned' in j) ):
        dropList.append(i)

#TODO: drop rows from dropList

print("\n\nPrevious Unique values:  ",dt["Fracture Type"].unique())

#Cleaning for fracture type
dropListF = []

for i,j in enumerate(dt["Fracture Type"]):
    
    if( ("Cone" in j) and ("Shear" in j) ):
        dt.loc[i,'Fracture Type'] = "Cone and Shear"
    elif( ("Cone" in j) and ("Split" in j) ):
        dt.loc[i,'Fracture Type'] = "Cone and Split"
    elif( ("Shear" in j) or ("SheaR" in j) ):
        dt.loc[i,'Fracture Type'] = "Shear"
    elif("Cone" in j):
        dt.loc[i,'Fracture Type'] = "Cone"
    elif( ("Columnar" in j) or ("Columner" in j) ):
        dt.loc[i,'Fracture Type'] = "Columnar"
    elif( "Combined" in j):
        dropListF.append(i)


print(" \n\nNew Unique values:  ",dt["Fracture Type"].unique())    
#TODO drop rows from dropListF
        
        
        
        
        
        