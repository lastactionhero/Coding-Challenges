#%%
# Find pair of 2 number whose sum is same as target
import numpy as np
from sqlalchemy import null
# %%
given_array = np.array([1,3,7,4,9,2])
target = 11
# %%
def find_second_position(first_num,target,arr):
    second_position =0
    second_number = target - first_num
    for num in arr:
        if num == second_number:
            return second_position
        second_position+=1
    return null


# %%
# 2 pointer technique
first_position = 0
second_position = null
for num in given_array:
    # pass array to function starting with next number to the first selected number (trimmed array)
    second_position = find_second_position(num,target,given_array[first_position+1:])
    if(second_position!=null):
        # We have sent trimmed array to function, hence recalculate actual position of second number 
        print(f'Positions {first_position} and {first_position + second_position + 1}')
        break
    first_position+=1
if(second_position == null):
    print(f'No pair found with sum as {target}')

# %%
