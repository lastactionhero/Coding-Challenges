#%%
from typing import List
#%%
def GetMaxContinuousProduct(nums) -> int :
    min_product = nums[0]
    max_product = nums[0]
    ans = nums[0]
    for i in range(1,len(nums)):
       # print(f'{nums[i]} {min_product} {max_product} {ans}')
        if(nums[i]<0):
            min_product, max_product = max_product, min_product
        min_product = min(nums[i],min_product*nums[i])
        max_product = max(nums[i],max_product*nums[i])
        ans= max(min_product,max_product)
        print(f'{nums[i]} {min_product} {max_product} {ans}')
    return ans

     

#%%
arr = [9, 6, 10, 3]
print(GetMaxContinuousProduct(arr))
# %%
