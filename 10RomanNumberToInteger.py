#%%
datadict = {'I':1,'V' :5 ,'X':10,'L':50,'C':100,'D':500,'M':1000 }
def RomanToNumeric(str) -> int:
    i=0
    str = str.upper()
    result=0
    while(i<len(str)):
        # check if next number is greater if yes then duduct current number from next and add to result. 
        if(i<len(str)-1 and str[i+1]>str[i]):
            result+= datadict[str[i+1]] - datadict[str[i]]
            i+=1
        else:
            result+=datadict[str[i]]
        i+=1
    
    return result

#%%
RomanToNumeric('ix')
# %%
