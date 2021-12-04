###
### Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
###
#%%
import numpy as np
#%%
# O(n^2) time complexity
area = 0
height = np.array([1,8,6,2,5,4,8,3,7])
for i,num in enumerate(height[:-1]):
    for j, num_second in enumerate(height[i+1:],start=i+1):
        h = min(num, num_second)
        l = j-i
        area = max(l*h, area)
       
print (f'area - {area}')

# %%
# Reduced complexity 
height = np.array([1,8,6,2,5,4,8,3,7])
forward = 0
area = 0
backward = len(height)-1
while(forward < backward):
    left = height[forward]
    right= height[backward]
    #print(f'{left} - {right} - {min(left, right) * (backward - forward)}')
    area = max(area , min(left, right) * (backward - forward))
    if(left < right):
        forward +=1
    else:
        backward-=1
print(area)

# %%
