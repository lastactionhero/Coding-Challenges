#%%
def BubbleSort(arr):
    n= len(arr)-1
    for j in range(n):
        for i in range(n-j):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1] = arr[i+1], arr[i]
    return arr

#%%
arr = [2, 23, 10, 1]
BubbleSort(arr)

# %%
