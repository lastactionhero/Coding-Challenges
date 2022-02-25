#%%
from sqlalchemy import false


def search(arr,val, upper, lower):
    
    if upper >= lower:
        mid = (upper+lower)//2
        print(f'{lower},{upper},{mid}')
        if(arr[mid]==val):
            return mid
        if(val < arr[mid]):
            upper = mid-1
        else:
            lower = mid+1
        return search(arr,val,upper, lower)
    else:
        return -1

#%%
# Find lower and upper bound in sorted array for repeated numbers
arr = [1,2,3,3,3,4,5,6,7,8]
num_to_search = 3
mid = search(arr,num_to_search,len(arr)-1,0)
u=mid+1
l=mid-1
j=len(arr)-1
has_found_low, has_found_high = False,False
for i in range(0,j):
    if(not has_found_low and arr[l]==num_to_search):
        l-=1
    else:
        has_found_low=True
    
    if(not has_found_high and arr[u]==num_to_search):
        u+=1
    else:
        has_found_high=True
    
    if has_found_high and has_found_low:
        exit

print(f'{l+1},{u-1}')
# %%
