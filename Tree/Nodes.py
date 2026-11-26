class Node:
    def __init__ (self,value):
        self.left=None
        self.right=None
        self.data=value

class BST:
    cnt=0
    def __init__ (self):
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

    def preorder(self,rt):
        if rt is None:
            return 
        else:
            print(rt.data,end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)

    def postorder(self,rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data,end=" ")

    def find_min_max(self,rt):
        temp=rt
        while temp.left is not None:
            temp=temp.left
        print("minimum value in BST is:", temp.data)
        temp=rt
        while temp.right is not None:
            temp=temp.right
        print("Maximum Value In BST is:",temp.data)

    def search(self,key):
        temp=self.root
        while temp:
            if temp.data==key:
                return True
            elif key<temp.data:
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
                self.count_leaf(rt.left)
                self.count_leaf(rt.right)

    def nodes(self,rt):
        if rt is None:
            return
        else:
            self.nodes(rt.left)
            self.cnt+=1
            self.nodes(rt.right)
    

b1=BST()

b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(0))
b1.insert(Node(65))
b1.insert(Node(300))

print("inorder Of Tree:")
b1.inorder(b1.root)

print("\npreorder of Tree:")
b1.preorder(b1.root)

print("\nPostorder Of Tree:")
b1.postorder(b1.root)

b1.find_min_max(b1.root)

if b1.search(0):
    print("\nFound The Node")
else:
    print("Not Found")

b1.cnt =0 
b1.count_leaf(b1.root)
print("total no. of leaf nodes:",b1.cnt)

b1.cnt =0 
b1.count_nleaf(b1.root)
print("total no. of Non-leaf nodes:",b1.cnt)

b1.cnt=0
b1.nodes(b1.root)
print("total no. of nodes",b1.cnt)