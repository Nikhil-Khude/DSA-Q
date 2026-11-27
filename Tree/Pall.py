class node:
    def __init__ (self,value):
        self.left=None
        self.right=None
        self.data=value
class BST:
    cnt=0
    def __init__(self):
        self.root=None

    def insert(self,new_node):
        if self.root is None:
            self.root=new_node
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data:
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else:
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right
        
    
    def inorder(self,rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data,end=" ")
            self.inorder(rt.right)


    def postorder(self,rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data,end=" ")

    def preorder(self,rt):
        if rt is None:
            return
        else:
            print(rt.data,end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)

    def Min_max(self,rt):
        temp=rt
        while temp.left is not None:
            temp=temp.left
        print("\nMin Node Of Tree:",temp.data)
        temp=rt
        while temp.right is not None:
            temp=temp.right
        print("\nMax Node of Tree:",temp.data)

    def search(self,value):
        temp=self.root
        while True:
            if temp.data==value:
                return True
            elif temp.data>value:
                temp=temp.left
            else:
                temp=temp.right
            return False

    def count_leaf(self,rt):
        if rt is None:
            return
        else:
            if rt.left is None and rt.right is None:
                self.cnt+=1
            self.count_leaf(rt.left)
            self.count_leaf(rt.right)

    def count_nleaf(self,rt):
        if rt is None:
            return
        else:
            if rt.left is not None and rt.right is not None:
                self.cnt+=1
            self.count_nleaf(rt.left)
            self.count_nleaf(rt.right)

    def count_nodes(self,rt):
        if rt is None:
            return
        else:
            self.count_nodes(rt.left)
            self.cnt+=1
            self.count_nodes(rt.right)

    def level_order(self,rt):
        if rt is None:
            print("BST is empty")
        else:
            arr=[]
            cnt=0
            arr.append(rt)
            while cnt<len(arr):
                temp=arr[cnt]
                cnt+=1
                print(temp.data,end=" ")
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)



b1=BST()
b1.insert(node(50))
b1.insert(node(30))
b1.insert(node(70))
b1.insert(node(20))
b1.insert(node(40))
b1.insert(node(60))
b1.insert(node(80))
print("Inorder Of Tree:-")
b1.inorder(b1.root)
print("\nInorder Of Tree:-")
b1.preorder(b1.root)
print("\nInorder Of Tree:-")
b1.postorder(b1.root)


b1.Min_max(b1.root)

if b1.search(90):
    print("\nNode Found")
else:
    print("\nNot Found")

cnt=0
b1.count_leaf(b1.root)
print("Count Of Leaf Node:-",b1.cnt)


cnt=0
b1.count_nleaf(b1.root)
print("\nCount Of Non-Leaf",b1.cnt)


cnt=0
b1.count_nodes(b1.root)
print("\nCount Of Nodes",b1.cnt)


b1.level_order(b1.root)