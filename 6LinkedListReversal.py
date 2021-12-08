#%%
import numpy as np
#%%
class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)

def PrintList(lnklst):
    while(True):    
        print(lnklst)
        if(lnklst.next == None):
            break
        lnklst=lnklst.next

# %%
head = ListNode(val=1)
h = head
for i in np.arange(2,11):
    n = ListNode(val = i)
    h.next=n
    h=n
#%%
PrintList(head)
#%%
curpos = 1
curnode = head
start = head
m=3
n=6
while(curpos < m):
    start = curnode
    curnode = curnode.next
    curpos+=1

newlist = None
tail = curnode
print(f'{start}, {tail}')
while(curpos >= m and curpos <= n):
    next = curnode.next
    curnode.next = newlist
    newlist = curnode
    curnode = next
    curpos+=1
print(f'{start}, {tail}')
start.next= newlist
tail.next = curnode
PrintList(head)
# %%

# %%
