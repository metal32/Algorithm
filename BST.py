"""                                     Binary Search Tree is an abstract data type      (priority queue)                                          """
## Arrays has binary search that can be done in O(logn) time but the insertion at the point leads to O(n) so total O(nlogn)
## Similarly in heaps it will take O(n) time to complete the above process i.e. insertion and checking the checkas it insert at the last then 
## you use maxheapify in O(logn) and after that search on the other side makes it total O(n)

### Binary tree property.( Priority Queue)
### Can perform insert, delete, find min/max and find next large or next smaller
### Binary tree node has one key, one left pointer, one right pointer and one parent pointer.
### Binary trees generally has asymtotic time of O(h) where h is the length of the longest path from the root to the leaf.
### Height of any node = {max(height of left child, heightof right child)}+1
### Size of a subtree is maintained by data augmentation 
### Binary trees are required for fast insertion, Balanced Binary trees have insertion in a sorted list of "O(logn)" even after having some kind oc check


###How to keep your trees balanced: By using AVL, AVL using rotation, it rotates the pointer
### Property of AVL tree is that the height of left child and right child differ max by +1 or-1.

### Inorder Transsverse has O(n)
### 1 insertions takes O(logn) and all the n insertions will take O(nlogn)

class BST(object):
    def __init__(self,key):
        self.val=key
        self.right=None
        self.left=None
        self.parent=None
        self.min=self
    def insert(self,k):
        new=BST(k)
        if self is None:
            self=new
        else:
            if k<self.val:
                if new.val < self.min.val:
                    self.min=new
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
            if self.parent is not None and self.parent.right is self:
                self=self.parent
                return self.parent
            else:
                return self.parent
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
