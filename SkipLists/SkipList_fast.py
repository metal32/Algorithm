import math
import random

class skipList:
    def __init__(self,maxsize=65535):
        self.maxLevel=int(math.log(maxsize,2))
        self.head=self._createNode(self.maxLevel,None,None)
        self.level=0
        self.Nil=self._createNode(-1,None,None)
        self.tail=self.Nil
        self.head[3:]=[self.Nil for x in range(self.maxLevel)]
        self._update=[self.head]*(1+self.maxLevel)
        self.p=1/math.e

    def _createNode(self,height,key,value):
        node=[None]*(4+height)
        node[0]=key
        node[1]=value
        return node

    def _randomHeight(self):
        lvl=0
        maxlevel=min(self.maxLevel,self.level+1) 
        while random.random()<self.p and lvl<maxlevel:
            lvl+=1
        return lvl

    def _findless(self,update,searchKey):
        node=self.head
        for i in xrange(self.level,-1,-1):
            key=node[3+i][0]
            while key is not None and key<searchKey:
                node=node[3+i]
                key=node[3+i][0]
            update[i]=node
        return node

    def insert(self,searchKey,value):
        assert searchKey is not None
        update=self._update[:]
        node=self._findless(update,searchKey)
        prev=node
        node=node[3]
        if node[0]==searchKey:
            node[1]=value
        else:
            lvl=self._randomHeight()
            self.level=max(self.level,lvl)
            node=self._createNode(lvl,searchKey,value)
            node[2]=prev
            for i in range(0,lvl+1):
                node[3+i]=update[i][3+i]
                update[i][3+i]=node
            if node[3] is self.Nil:
                self.tail=node
            else:
                node[3][2]=node

    def delete(self,searchKey):
        update=self._update[:]
        node=self._findless(update,searchKey)
        node=node[3]
        if node[0]==searchKey:
            node[3][2]=update[0]
            for i in range(self.level+1):
                if update[i][3+i] is not node:
                    break
                update[i][3+i]=node[3+i]
            while self.level>0 and self.head[3+self.level][0] is None:
                self.level-=1
            if self.tail is node:
                self.tail=node[2]
            return True

    def search(self,searchKey):
        node = self.head
        for i in xrange(self.level, -1, -1):
            key = node[3 + i][0]
            while key is not None and key < searchKey:
                node = node[3 + i]
                key = node[3 + i][0]
        node = node[3]
        if node[0] == searchKey:
            return node[1]

l=skipList()

for i in range(2,11):
    l.insert(i,'Hostel:'+str(i))

print l.delete(2)
print l.search(2)


