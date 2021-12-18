#%%
import pickle
import sys
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
    
    def inorderTraversalNodeList(self, root):
        result = []
        if(root is not None):
            result.append(root)
            result += self.inorderTraversalNodeList(root.left)
            result += self.inorderTraversalNodeList(root.right)
        return result

# This class is responsible for serializing tree, 
# deserializing and constructing tree
class Transporter:
    def printError(self):
        type, value, traceback = sys.exc_info()
        print(f'{type}, {value}, {traceback}')
    
    # Serialize tree node objects, with in-order traversal. This way root will be first object.
    def serializeTree(self, root):
        try:
            result = root.inorderTraversalNodeList(root)
        except:
            printError()
            return
        
        try:
            with open('Tree.txt', mode='wb') as file :
                pickle.dump(result, file) 
        except:
            printError()
        finally:
            file.close()
    # Here we deserialize list of node objects of tree. 
    # They have already referencing each other at the time of serialization.
    # Hence deserialize all objects and return only first one (root)        
    def deserializeTree(self):
        try:
            with open('Tree.txt', mode='rb') as file:
                result = pickle.load(file)
        except:
            printError()
        finally:
            file.close()

        return result[0]
    
 
# %% Built tree from input array
inputArray = [20, 40, 10, 60, 80, 30]
r = None
for num in inputArray:
    if r is None:
        r = Node(num)
    else:
        r.insertNode(num)

print(f'This is the b-tree sent to serialization - \n{r.inorderTraversal(r)}')

t = Transporter()
# Serialize
t.serializeTree(r)
# deserialize into tree node
root = t.deserializeTree()
print(f'This is the b-tree retrieved after deserialization - \n{root.inorderTraversal(root)}')

# %%
