#%%
import numpy as np
from sqlalchemy import null, true
#%%
given_array = np.array([1,3,7,4,9,2])
target = 11
#%%
# Create dictionary
search_num ={}
index = 0
for num in given_array:
    search_for = target - num
    if(search_num.get(search_for) != None):
        print(f'{search_num.get(search_for)} , {index}')
        break
    search_num[search_for]= index
    index+=1

# %%
