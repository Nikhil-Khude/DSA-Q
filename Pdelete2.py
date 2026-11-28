class Node:
    def __init__ (self,value):
        self.left=None
        self.right=None
        self.data=value
class BST():
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

