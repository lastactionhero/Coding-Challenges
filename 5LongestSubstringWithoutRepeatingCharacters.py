#%%
# from collections import deque
s = 'abcbdca'
# longestsubstring = deque()
stringmap = dict()
longestlength = 0
begining = 0
end = 0
for index, ch in enumerate(s):
    if((stringmap.get(ch) != None) and (stringmap[ch] >= begining)):
        begining = stringmap[ch]+1
    stringmap[ch]=index
    end+=1
    longestlength=max(longestlength, end-begining)
print(f'longest substring length is {longestlength}')
# %%
