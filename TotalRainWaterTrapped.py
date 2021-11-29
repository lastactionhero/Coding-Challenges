#%%
#height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [0,1,0,2,0,0,4]
# calculate height of water on each number. 
# water that each number can store is - 
# min(max(height of left to number in array) , max( height of right to number)) - number
l = len(height)
water = 0
#print(l)
for index, num in enumerate(height):
    #print(f'{index},  {num}')
    maxleft=num if (index == 0) else max(height[0:index],default=0)
    maxright=num if (index==l) else max(height[index+1:l],default=0)
    capacity =  0 if (min(maxleft, maxright) - num) <0 else (min(maxleft, maxright) - num)
    water += capacity
    #print(f'num = {num}, index = {index} , max left = {maxleft} , max right {maxright} , water = {capacity}')
print(water)
# %%
h=[1,2,3,4,5,6,7,8,9]
h[2:9]
# %%
