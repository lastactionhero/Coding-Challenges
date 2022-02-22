#%%
input = [1, 8, 3, 0, 2, 0]
# 2 pointer approach
i,j=0,0
while (i<len(input)):
    print(f'{input[i]} , {i}, {j}')
    if(input[i]!=0):
        input[j],input[i] = input[i],input[j]
        j+=1
    i+=1


print(input)


#%%
print (f'{i},{j}')
# %%
