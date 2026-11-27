class node:
    def __init__ (self,value):
        self.right=None
        self.left=None
        self.data=value

class bst:
    def __init__(self):
        self.root= None

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


    def inoreder(self,rt):
        if rt is None:
            return
        else:
            self.inoreder(rt.left)
            print(rt.data,end=" ")
            self.inoreder(rt.right)

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
        while temp is not None:
            if temp.data==key:
                return True 
            elif key<temp.data:
                temp=temp.left
            else:
                temp=temp.right
        return False

    def min_max(self,rt):
        temp=rt
        if rt.left is not None:
            temp=temp.left
        print("Minimun value in BST is:-",temp.data)
        temp=rt
        if temp.right is not None:
            temp=temp.right
        print("Maximum Value in BST is:-",temp.data)


    
b1=bst()
b1.insert(node(45))
b1.insert(node(25))
b1.insert(node(65))
b1.insert(node(15))
b1.insert(node(35))
b1.insert(node(55))
b1.insert(node(75))
b1.insert(node(10))
b1.insert(node(30))
print("Inorder of Tree:-")
b1.inoreder(b1.root)
print("\nPreorder of Tree:-")
b1.preorder(b1.root)
print("\nPostorder of Tree:-")
b1.postorder(b1.root)

if b1.search(76):
    print("\nNode Founded")
else:
    print("\nNot Found")

b1.min_max(b1.root)