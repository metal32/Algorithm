
class BST(object):
    def __init__(self,key):
        self.val=key
        self.right=None
        self.left=None
        self.parent=None
    def insert(self,k):
        new=BST(k)
        if self is None:
            self=new
        else:
            if k<self.val:
                if self.left is None:
                    new.parent=self
                    self.left=new
                else:
                    self.left.insert(k)
            else:
                if self.right is None:
                    new.parent=self
                    self.right=new
                else:
                    self.right.insert(k)
    def find(self,k):
        if self.val==k:
            return self
        else:
            if k<self.val:
                if self.left is None:
                    print "Not in BST"
                    return None
                else: 
                    return self.left.find(k)
            else:
                if self.right is None:
                    print "Not in BST"
                    return None
                else:
                    return self.right.find(k)
    def find_min(self):
        if self.left is None:
            return self
        else:
            return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self
        else:
            return self.right.find_max()
    def find_secondmax(self):
        if self.right is None:
            if self.left is None:
                return self.parent
            else:
                return self.left.find_max()
        else:
            return self.right.find_secondmax()
    def find_secondmin(self):
        if self.left is None:
            if self.right is None:
                return self.parent
            else:
                return self.right.find_min()
        else:
            return self.left.find_secondmin()
    def next_larger(self):
        if self.right is not None:
            return self.right.find_min()
        else:
            current=self
            while current.parent is not None and current.parent.right is current:
                current=current.parent
            return current.parent
           
    def delete(self,k):
        self=self.find(k)
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return "Deleted"
        else:
                d=self.next_larger()
                self.val,d.val=d.val,self.val
                return d.delete(d.val)
def inorder(s):
    if s:
        inorder(s.left)
        print s.val
        inorder(s.right)
   
 
s=BST(50)
s.insert(40)
s.insert(30)
s.insert(35)
s.insert(32)
s.insert(38)
s.insert(67)
s.insert(57)
s.insert(68)
s.insert(52)
s.insert(59)
s.insert(65)
s.insert(69)
s.insert(31)
print s.find_min().val
print s.find_max().val
print s.find_secondmax().val
print s.find_secondmin().val

s.delete(31)
print "\nAfter deletion \n"

print s.find_min().val
print s.find_max().val
print s.find_secondmax().val
print s.find_secondmin().val
print "\n"
inorder(s)
