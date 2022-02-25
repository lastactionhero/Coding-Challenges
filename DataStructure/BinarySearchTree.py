#%%
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if(self.data):
            if(data<self.data):
                if(self.left):
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if(self.right):
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self = Node(data)
    
    def findval(self, data):
        if(data<self.data):
            if(self.left):
                self.left.findval(data)
            else:
                print(f'{data} not found')
        elif(data>self.data):
            if(self.right):
                self.right.findval(data)
            else:
                print(f'{data} not found')
        else:
            print(f'{data} found')       
    
    def printtree(self):
        if(self.left):
            self.left.printtree()
        print(self.data)
        if(self.right):
            self.right.printtree()
#%%
root = Node(5)
root.insert(3)
root.insert(2)
root.insert(6)
root.insert(4)
print(root.printtree())
# %%
root.findval(33)
# %%
