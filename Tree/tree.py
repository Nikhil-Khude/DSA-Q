# BST using linked list 
class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None

class BST:
    cnt = 0 
    def __init__(self):
        
        self.root=None
    def insert(self,new_node):
        if self.root is None: # Tree is empty (No node in BST)
            self.root=new_node
        else:
            temp = self.root 
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return 
                    else:
                        temp = temp.left 
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return 
                    else:
                        temp = temp.right 

    

    
    def inorder(self,rt):
        if rt is None:
            return 
        else:
            self.inorder(rt.left)
            print(rt.data, end = " ")
            self.inorder(rt.right)

    def count_leaf(self,rt):
        if rt is None:
            return
        else:
            if rt.left is None and rt.right is None:
                self.cnt += 1
            self.count_leaf(rt.right)
            self.count_leaf(rt.left)
            
    def count_nleaf(self,rt):
        if rt is None:
            return 
        else:
            
            if rt.left is not None or rt.right is not None: 
                self.cnt += 1
                self.count_nleaf(rt.left)
                self.count_nleaf(rt.right)

    def count(self,rt):
        if rt is None:
            return
        else:
            self.count(rt.left)
            self.cnt += 1
            self.count(rt.right)
             

    def preorder(self,rt):
        if rt is None:
            return 
        else:
            print(rt.data, end = " ")
            self.preorder(rt.left)
            self.preorder(rt.right)
    def postorder(self,rt):
        if rt is None:
            return 
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end = " ")

    def findminmax(self,rt):
        temp = rt
        while temp.left is not None:
            temp=temp.left
        print("minimum value in BST is:", temp.data)
        temp = rt 
        while temp.right is not None:
            temp = temp.right
        print("maximum value in BST is:", temp.data)

    def level_order(self,rt):
        if rt is None:
            print("BST is empty")
        else:
            arr = []
            cnt = 0
            arr.append(rt)
            while(cnt<len(arr)):
                temp = arr[cnt]
                cnt +=1
                print(temp.data,end = " ")
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)


    def search (self,key):
        temp = self.root 
        while temp:
            if temp.data == key:
                return True
            elif key < temp.data:
                temp = temp.left 
            else:
                temp = temp.right 
        return False 
    

b1=BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))
print("\nInorder:")
b1.inorder(b1.root)
print("\npreorder:")
b1.preorder(b1.root)
print("\nPostorder:")
b1.postorder(b1.root)
print("\nMinimum and Maximum value in BST is:")
b1.findminmax(b1.root)           
if b1.search(0):
    print("\nFound the node:")
else:
    print("\nNot found:")

b1.cnt =0 
b1.count_leaf(b1.root)
print("total no. of leaf nodes:",b1.cnt)
b1.cnt =0 

b1.count_nleaf(b1.root)
print("\nTotal no. of non leaf nodes:",b1.cnt)
b1.cnt =0 

b1.count(b1.root)
print("\ncount of nodes:", b1.cnt)
print("\nlevel order:")
b1.level_order(b1.root)