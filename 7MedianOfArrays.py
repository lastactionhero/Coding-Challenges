# %%
# Input
a=[1,2,3]
b=[5,6,7]

# Solution
# Calculate lengths of arrays and total lenght of both arrays combined
from collections import deque
al = len(a)
bl = len(b)
l = al + bl
middle1, middle2 = 0,0
if (l%2 == 0):
    #even
    middle1, middle2 = l//2, l//2+1
else:
    #odd
    middle1, middle2 = l//2+1, l//2+1
print(f'{middle1}, {middle2}')
# %%

midnum1 , midnum2= None, None
num1, num2 = -1, -1
p1,p2 = 0,0
# End loop once we get medium2 (second number in median calculation)
while(midnum2 is None ):
    if((p1)==al):
        # This means we have reached to end of first array. 
        # Hence compare same number from second array.
        num1, num2 = b[p2],b[p2]
    elif((p2)==bl):
        # This means we have reached to end of second array. 
        num1, num2 = a[p1],a[p1]
    else:
        num1, num2 = a[p1],b[p2]

    smallerNum = min(num1, num2)
    if (p1+p2+1) == middle1:
        midnum1 = smallerNum
    if (p1+p2+1) == middle2:
        midnum2 = smallerNum

    if ((p1)<al) and (a[p1]<b[p2]):
        p1+=1
    else:
        if((p2)<bl):
            p2+=1

Median = (midnum1 + midnum2)/2

print(f'{Median}')
# %%
