#%%
import pickle
#%%
# This class is responsible for serializing tree, 
# deserializing and constructing tree
class Transporter:
    def builtTree(self, arr):
        r = None
        for num in inputArray:
            if r is None:
                r = Node(num)
            else:
                r.insertNode(num)
        return r
    
    def serializeTree(self, root):
        result = root.inorderTraversal(root)
        file = open('Tree.txt', mode='wb')
        pickle.dump(result, file)
        file.close() 
    
    def deserializeTree(self):
        file = open('Tree.txt', mode='rb')
        result = pickle.load(file)
        file.close()
        return self.builtTree(result)
    
    

# this is tree node with inorder traversal
class Node:
    def __init__(self, data:int):
        self.left = None
        self.right = None
        self.data = data

    def display(self):
        if(self.left is not None):
            self.left.display()
        
        print(self.data)
        if(self.right is not None):
            self.right.display()

    def insertNode(self, d:int):
        if(d<self.data):
            # d should be inserted to left of the node
            if(self.left is None):
                self.left = Node(d)
            else:   
                self.left.insertNode(d)
        else:
            # d should be inserted to right
            if(self.right is None):
                self.right = Node(d)
            else:
                self.right.insertNode(d)
    
    def inorderTraversal(self, root):
        result = []
        if(root is not None):
            result.append(root.data)
            result += self.inorderTraversal(root.left)
            result += self.inorderTraversal(root.right)
        return result
        
  

# %% Built tree from input array
inputArray = [5, 3, 2, 10, 7]
r = None
for num in inputArray:
    print(num)
    if r is None:
        r = Node(num)
    else:
        r.insertNode(num)

t = Transporter()
# Serialize
t.serializeTree(r)
# deserialize into tree node
root = t.deserializeTree()
# check deserialization
print(root.inorderTraversal(root))
