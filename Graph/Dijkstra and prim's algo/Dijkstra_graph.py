import sys
class Vertex(object):
    def __init__(self,key):
        self.id=key
        self.connectedTo={}
        self.level={self:0}
        self.parent=None
        self.color="white"
        self.discovery=0
        self.finish=None
        self.distance=sys.maxint

    def setDistance(self,x):
        self.distance=x

    def getDistance(self):
        return self.distance

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr]=weight

    def __str__(self):
        return str(self.id)+' connected to '+str([x.id for x in self.connectedTo])
    
    def setPred(self,s):
        self.parent=s

    def getPred(self):
        return self.parent

    def setColor(self,col):
        self.color=col

    def getColor(self):
        return self.color

    def setDiscovery(self,time):
        self.discovery=time

    def getDiscovery(self):
        return self.discovery

    def setFinish(self,time):
        self.finish=time

    def getFinish(self):
        return self.finish
    
    def getConnection(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph(object):
    def __init__(self):
        self.vertList={}
        self.numVertices=0
        self.edges={}

    def setEdge(self,f,t,u):
        self.edges[(f,t)]=u

    def addVertex(self,key):
        self.numVertices+=1
        newVertex=Vertex(key)
        self.vertList[key]=newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self):
        return n in self.vertList

    def getVertices(self):
        return self.vertList.keys()
    
    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv=self.addVertex(f)
        if t not in self.vertList:
            nv=self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t],cost)

    def __iter__(self):
        return iter(self.vertList.values())


class PriorityQueue(Graph):
    def __init__(self):
        Graph.__init__(self)
        self.heapList=[0]
        self.key={}
        self.currentSize=0

    def addKeys(self,alist,g):
        for v in g:
            for i in alist:
                if v in i:
                    self.key[v]=i

    def percUp(self,i):
        while i//2>0:
            if self.heapList[i]<self.heapList[i//2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i=i//2

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

    def heapSort(self):
        alist=[]
        i=self.currentSize
        while i>0:
            alist.append(self.delMin())
            i-=1
        return alist

    ## this function is only used in Dijkstra
    def decreaseKey(self,Vertex,dist):
        a,b=self.key[Vertex]
        i=self.heapList.index((a,b))
        a=dist
        self.heapList[i]=(a,b)
        self.key[Vertex]=(a,b)
        self.percUp(i)

    def isEmpty(self):
        if self.currentSize==0:
            return True
        else: 
            return False