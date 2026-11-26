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


b1.cnt =0 
b1.count_leaf(b1.root)
print("total no. of leaf nodes:",b1.cnt)


b1.cnt =0 
b1.count_nleaf(b1.root)
print("total no. of Non-leaf nodes:",b1.cnt)