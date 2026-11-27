class node:
    def __init__ (self,value):
        self.left=None
        self.right=None
        self.data=value

class BST:
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

    def Min_max(self,rt):
        temp=rt
        while temp.left is not None:
            temp=temp.left
        print("\nMinimum Score",temp.data)
        temp=rt
        while temp.right is not None:
            temp=temp.right
        print("\nMaximum Score",temp.data)

    def search(self,key):
        temp=self.root
        while temp is not None:
            if temp.data==key:
                return True
            elif temp.data>key:
                temp=temp.left
            else:
                temp=temp.right
        return False

    def searchScore(self,rt):
        if rt is None:
            return 0
        else:
            count=0
            if rt.data>50:
                count+=1
            return(count+
            self.searchScore(rt.left)+
            self.searchScore(rt.right))

    def cal_sum(self,rt):
        if rt is None:
            return 0
        else:
            return (rt.data + 
                    self.cal_sum(rt.right) +
                    self.cal_sum(rt.left))
        
    def countnodes(self,rt):
        if rt is None:
            return 0
        else:
            return(1+
             self.countnodes(rt.left)+
             self.countnodes(rt.right))

    def findavg(self):
        total=self.cal_sum(self.root)
        count=self.countnodes(self.root)

        if count==0:
            return 0
        return total/count


b1=BST()
b1.insert(node(45))       
b1.insert(node(78))      
b1.insert(node(32))      
b1.insert(node(89))      
b1.insert(node(56))      
b1.insert(node(92))   
b1.insert(node(67))      
b1.insert(node(34))      
b1.insert(node(85))                  
b1.insert(node(73))      
b1.insert(node(61)) 
b1.insert(node(98))
print("\nscores in ascending order")
b1.inorder(b1.root)    
b1.Min_max(b1.root)

if b1.search(87):
    print("Score Founded")
else:
    print("Not Founded")

print("Students Scoring Above 50:",
      b1.searchScore(b1.root))

print("\nTotal Marks:", b1.cal_sum(b1.root))
print("\nTotal Nodes:", b1.countnodes(b1.root))
print("\nAverage:", b1.findavg())