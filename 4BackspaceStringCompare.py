#%%
from collections import deque
import string
# %%
lifo = deque()
lifo.append('a')
lifo.append('b')
print(lifo)
# %%
print(len(lifo))
# %%
print(lifo)
#%%
def TypeoutString(str):
    lifo = deque()
    for ch in str:
        if(ch == '#'):
            if(len(lifo)>0):
                lifo.pop()
            else:
                continue
        else:
            lifo.append(ch)
    return lifo
         

# %%
s, t = "ab#", "A"
print(TypeoutString(t))
TypeoutString(t) == TypeoutString(s)
# %%
