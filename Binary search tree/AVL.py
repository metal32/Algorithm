class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor=0

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

class BinarySearchTree(TreeNode):

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
                   self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                   self.updateBalance(currentNode.rightChild)

    def updateBalance(self,node):
        if node.balanceFactor>1 or node.balanceFactor<-1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor+=1
            elif node.isRightChild():
                node.parent.balanceFactor-=1
            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rotateLeft(self,rotRoot):
        newRoot=rotRoot.rightChild
        rotRoot.rightChild=newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent=rotRoot
        newRoot.parent=rotRoot.parent
        if rotRoot.isRoot():
            self.root=newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild=newRoot
            else:
                rotRoot.parent.rightChild=newRoot
        newRoot.leftChild=rotRoot
        rotRoot.parent=newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    def rotateRight(self,rotRoot):
        newRoot=rotRoot.leftChild
        rotRoot.leftChild=newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent=rotRoot
        newRoot.parent=rotRoot.parent
        if rotRoot.isRoot():
            self.root=newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild=newRoot
            else:
                rotRoot.parent.rightChild=newRoot
        newRoot.rightChild=rotRoot
        rotRoot.parent=newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - max(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + min(rotRoot.balanceFactor, 0)

    def rebalance(self,node):
        if node.balanceFactor<0:
            if node.rightChild.balanceFactor>0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor>0:
            if node.leftChild.balanceFactor<0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)


    def __setitem__(self,k,v):
       self.put(k,v)

    def get(self,key):
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.payload
           else:
                  return None
       else:
           return None

    def _get(self,key,currentNode):
       if not currentNode:
           return None
       elif currentNode.key == key:
           return currentNode
       elif key < currentNode.key:
           return self._get(key,currentNode.leftChild)
       else:
           return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
       return self.get(key)

    def __contains__(self,key):
       if self._get(key,self.root):
           return True
       else:
           return False

    def updateBalanceDel(self,node):
        if node.balanceFactor<-1 or node.balanceFactor>1:
            self.rebalance(node)
            return
        if node.parent:
            if node.isLeftChild():
                node.parent.balanceFactor-=1
            elif node.isRightChild():
                node.parent.balanceFactor+=1
            if node.parent.balanceFactor==0:
                self.updateBalance(node.parent)

    def delete(self,key):
      if self.size > 1:
         nodeToRemove = self._get(key,self.root)
         if nodeToRemove:
             self.remove(nodeToRemove)
             self.size = self.size-1
         else:
             raise KeyError('Error, key not in tree')
      elif self.size == 1 and self.root.key == key:
         self.root = None
         self.size = self.size - 1
      else:
         raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
       self.delete(key)


    def remove(self,node):
        if node.isLeaf():
            if node.isLeftChild():
                node.parent.leftChild=None
                node.parent.balanceFactor-=1
                if node.parent.balanceFactor==0:
                    self.updateBalanceDel(node.parent)
            else:
                node.parent.rightChild=None
                node.parent.balanceFactor+=1
                if node.parent.balanceFactor==0:
                    self.updateBalanceDel(node.parent)

        elif node.hasBothChildren():
            succ=node.findSuccessor()
            succ.spliceOut()
            node.key=succ.key
            node.payLoad=succ.payLoad
            if succ.isLeftChild():
                succ.parent.balanceFactor-=1
                if succ.parent.balanceFactor==0:
                    self.updateBalanceDel(succ.parent)
            else:
                succ.parent.balanceFactor+=1
                if succ.parent.balanceFactor==0:
                    self.updateBalanceDel(succ.parent)
        else:
            if node.hasLeftChild():
                if node.isLeftChild():
                    node.parent.leftChild=node.leftChild
                    node.leftChild.parent=node.parent
                    node.parent.balanceFactor-=1
                    if node.parent.balanceFactor==0:
                        self.updateBalanceDel(node.parent)
                elif node.isRightChild():
                    node.parent.rightChild=node.leftChild
                    node.leftChild.parent=node.parent
                    node.parent.balanceFactor+=1
                    if node.parent.balanceFactor==0:
                        self.updateBalanceDel(node.parent)
                else:
                    node.replaceNodeData(node.leftChild.key,node.leftChild.payLoad,node.leftChild.leftChild,node.leftChild.rightChild)
            else:
                if node.isLeftChild():
                    node.rightChild.parent = node.parent
                    node.parent.leftChild = node.rightChild
                    node.parent.balanceFactor-=1
                    if node.parent.balanceFactor==0:
                        self.updateBalanceDel(node.parent)
                elif node.isRightChild():
                    node.rightChild.parent = node.parent
                    node.parent.rightChild = node.rightChild
                    node.parent.balanceFactor+=1
                    if node.parent.balanceFactor==0:
                        self.updateBalanceDel(node.parent)
                else:
                    node.replaceNodeData(node.rightChild.key,
                                    node.rightChild.payload,
                                    node.rightChild.leftChild,
                                    node.rightChild.rightChild)




s = BinarySearchTree()
s[1]='Ayush'
s[9]='Ashish'
s[3]='Rishabh'
s[6]="Chaman"
s[2]="Rishab"

s[7]="Kunal"
s[11]="Dhruv"
s[10]="Amandeep"
s[9]="Rahul"


print s.root.key
print s.root.balanceFactor
print s.root.parent