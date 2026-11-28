class Node:
    def __init__ (self,value):
        self.left=None
        self.right=None
        self.data=value
class BST():
    cnt=0
    def __init__(self):
        self.root=None

    def insert(self,New_node):
        if self.root is None:
            self.root=New_node
        else:
            temp=self.root
            while True:
                if New_node.data <temp.data:
                    if temp.left is None:
                        temp.left=New_node
                        return
                    else:
                        temp=temp.left
                else:
                    if temp.right is None:
                        temp.right=New_node
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

    def search(self,key):
        temp=self.root
        while temp:
            if temp.data==key:
                return True
            elif temp.data>key:
                temp=temp.left
            else:
                temp=temp.right
        return False

    def Min_max(self,rt):
        temp=rt
        while temp.left is not None:
            temp=temp.left
        print("\nMinimum Node Of Tree:-",temp.data)
        temp=rt
        while temp.right is not None:
            temp=temp.right
        print("\nMaximum Node Of Tree:-",temp.data)

    def count_nodes(self,rt):
        if rt is None:
            return
        else:
            self.count_nodes(rt.left)
            self.cnt+=1
            self.count_nodes(rt.right)

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
            if rt.left is not None or rt.right is not None:
                self.cnt+=1
                self.count_nleaf(rt.left)
                self.count_nleaf(rt.right)

    def get_successor(self,temp):
        temp=temp.right
        while temp is not None and temp.left is not None:
            temp=temp.left
        return temp

    def get_delete(self,rt,value):
        if rt is None:
            return
        else:
            if rt.data>value:
                rt.left=self.get_delete(rt.left,value)
            elif rt.data<value:
                rt.right=self.get_delete(rt.right,value)
            else:
                #for Node with 0 or 1 child
                if rt.left is None:
                    return rt.right
                if rt.right is None:
                    return rt.left
                # node with 2 child
                succ=self.get_successor(rt)
                rt.data=succ.data
                rt.right=self.get_delete(rt.right,succ.data)
            return rt




b1=BST()
b1.insert(Node(50))
b1.insert(Node(30))
b1.insert(Node(70))
b1.insert(Node(20))
b1.insert(Node(40))
b1.insert(Node(60))
b1.insert(Node(80))
b1.insert(Node(10))
b1.insert(Node(35))
b1.insert(Node(45))
b1.insert(Node(65))
b1.insert(Node(90))
print("\nInorder Of Tree:-")
b1.inorder(b1.root)

print("\nPreorder Of Tree:-")
b1.preorder(b1.root)

print("\nPostorder Of Tree:-")
b1.postorder(b1.root)

if b1.search(165):
    print("\nNode Found")
else:
    print("\nNode Not Found")


b1.Min_max(b1.root)

b1.cnt=0
b1.count_nodes(b1.root)
print("\nCount Of Nodes In Tree:-",b1.cnt)

b1.cnt=0
b1.count_leaf(b1.root)
print("\nCount Of Leaf Nodes In Tree:-",b1.cnt)

b1.cnt=0
b1.count_nleaf(b1.root)
print("\nCount Of Non-Leaf Nodes In Tree:-",b1.cnt)

b1.get_delete(b1.root,70)
print("After Deletion:-")
b1.inorder(b1.root)