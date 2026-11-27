class node:
    def __init__ (self,value):
        self.left=None
        self.right=None
        self.data=value
class BST:
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




