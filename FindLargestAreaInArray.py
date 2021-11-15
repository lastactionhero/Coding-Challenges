###
### Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
###
#%%
import numpy as np
#%%
area = 0
height = np.array([1,8,6,2,5,4,8,3,7])
for i,num in enumerate(height[:-1]):
    print(f'index- {i}, num - {num}') 
    for j, num_second in enumerate(height[i+1:],start=i+1):
        h = min(num, num_second)
        l = j-i
        area = max(l*h, area)
        print(f'{num}, {num_second}, {i},{j}, {h}')
       
print (f'area - {area}')

# %%
