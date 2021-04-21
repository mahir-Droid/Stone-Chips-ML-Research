# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:58:02 2020

@author: mahir
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

data = pd.read_excel('stonechipsdata.xlsx')



#data = data.dropna(subset=['Sample Location'],how='any')
data['Sample Location'] = data['Sample Location'].astype(str)

data['SI No.'] = pd.Series(data['SI No.']).fillna(method='ffill')
data['Sample Location'] = pd.Series(data['Sample Location']).fillna(method='ffill')
data['Construction Year'] = pd.Series(data['Construction Year']).fillna(method='ffill')
# Finding faulty comnined category in Sample Location
data['Sample Location'] = data['Sample Location'].astype(str)

data['Sample Location'] = pd.Series(data['Sample Location']).fillna(method='ffill')



#Dropping mixed values in Sample Location
dropList = [];

for i, j in enumerate(data['Sample Location']):
    if(  (('Beam' in j) or ('beam' in j)) and (('Column' in j) or ('column' in j)) ):
        print(i,'BnC')
        dropList.append(i)
        
    if(  (('Beam' in j) or ('beam' in j)) and (('Slab' in j) or ('slab' in j)) ):
        print(i,'BnS')
        dropList.append(i)
        
    if(  (('Column' in j) or ('column' in j)) and (('Slab' in j) or ('slab' in j)) ):
        print(i,'CnS')
        dropList.append(i)
 

data.drop(index = dropList, axis = 0, inplace = True)

    
    
''' 
for i in data.index: 
    j = data['Sample Location'].get(i)
    
    if(  (('Beam' in j) or ('beam' in j)) and (('Column' in j) or ('column' in j)) ):
        print(i,'BnC',j)
        data.drop(data.index[i], axis = 0, inplace = True)
        data = data.reset_index(drop=True)
    if(  (('Beam' in j) or ('beam' in j)) and (('Slab' in j) or ('slab' in j)) ):
        print(i,'BnS',j)
        data.drop(data.index[i], axis = 0, inplace = True)
        data = data.reset_index(drop=True)
    if(  (('Column' in j) or ('column' in j)) and (('Slab' in j) or ('slab' in j)) ):
        print(i,'CnS',j)
        data.drop(data.index[i], axis = 0, inplace = True)
        data = data.reset_index(drop=True)
'''    
    
            
data = data.reset_index(drop=True)



#Replacing Sample location with Column/Slab/Beam. 

for i, j in enumerate(data['Sample Location']):
    
    if(('Beam' in j) or ('beam' in j)):
        data.loc[i,'Sample Location'] = 'Beam'
    elif(('Column' in j) or ('column' in j)):
        data.loc[i,'Sample Location'] = 'Column'
    elif(('Slab' in j) or ('slab' in j)):
        data.loc[i,'Sample Location'] = 'Slab'
    

data['Sample Location'] = pd.Series(data['Sample Location']).fillna(method='ffill')  
        


data['Construction Year'].fillna('Missing', inplace=True)

data['Construction Year'] = data['Construction Year'].astype(str)


#Slicing Construction Year to keep only the upper bound of the Year Range.

for i, j in enumerate(data['Construction Year']):
    
    if('-' in j):
        ind = j.index('-')
        data.loc[i,'Construction Year'] = j[:ind]
        



#Dropping Rows with Quantity of Sample = 1

data.drop(data.loc[data['Quantity of Sample']==1].index, inplace=True)

        
  
      
print(data.head())
