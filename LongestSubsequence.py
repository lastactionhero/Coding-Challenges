#%%
import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...
def calculatePosition(str1, d, common):
    i=0
    for ch in str1:
        if ch not in list(common):
            i+=1
            continue
        if ch in d:
            d[ch]+=i
        else:
            d[ch]=i
        i+=1
    return d
# steps
# GEt common characters and find their positinal values in both arrays and sum that value. 
# from the output fine the longest increasing numbers location
# X,5 ; M,1 ; J,4 ; A,7 ; U,11 ; Z,7 in this dictionay only increasing longest sequeence is MJAU
#%%
for line in []:
    print(line, end="")
    # get both strings
    str1 = line.split(';')[0]
    str2 = line.split(';')[1].replace(f'\n','')
    s1 = set(str1)
    s2 = set(str2)
    common = s1.intersection(s2)
    print(common)
    charmap = {}
    calculatePosition(str1,charmap, common)
    calculatePosition(str2, charmap, common)
    
    ans =[]
    prev=0
    for key, value in charmap.items():
        if(prev<value):
            ans.append(key)
        else:
            prev = value
    print(ans)   
    # get the positional index
# %%

for a in range(0,3):
    print(a)
# %%
ar = range(0,10)
for a in ar[2:4]:
    print(a)
# %%
