import sys
class Vertex(object):
    def __init__(self,key):
        self.id=key
        self.connectedTo={}
        self.level={self:0}
        self.parent=[]
        self.color="white"
        self.discovery=0
        self.finish=None
        self.distance={}

    def setDistance(self,i,x):
        self.distance[i]=x

    def getDistance(self,i):
        return self.distance[i]

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr]=weight

    def __str__(self):
        return str(self.id)+' connected to '+str([x.id for x in self.connectedTo])
    
    def setPred(self,i,s):
        self.parent[i]=s

    def getPred(self,i):
        return self.parent[i]

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

class DFSGraph(Graph):
    def __init__(self):
        Graph.__init__(self)
        self.time=0
        self.order=[]

    def dfs(self):
        for aVertex in self:
            aVertex.setColor("white")
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self,aVertex):
        aVertex.setColor('gray')
        self.time+=1
        aVertex.setDiscovery(self.time)
        for newVertex in aVertex.getConnection():
            if newVertex.getColor() == 'white':
                newVertex.setPred(aVertex)
                Graph.setEdge(self,aVertex,newVertex,'tree')
                self.dfsvisit(newVertex)
            elif newVertex.finish==None:
                Graph.setEdge(self,aVertex,newVertex,'back')
            elif newVertex.discovery>aVertex.discovery:
                Graph.setEdge(self,aVertex,newVertex,'forward')
            else:
                Graph.setEdge(self,aVertex,newVertex,'cross')

        aVertex.setColor('black')
        self.time+=1
        aVertex.setFinish(self.time)
        self.order.append(aVertex)

    def topologicalSort(self):
        return self.order[::-1]

def Shortest_path_cyclic(aGraph,s):
    for i in range(aGraph.numVertices):
        s.setDistance(i,0)
        s.setPred(i,None)
    aGraph.dfs()
    order=aGraph.topologicalSort()
    for v in order:
        if v is not s:
            v.setDistance(0,sys.maxint)
    for v in order:
        sp_cycle_dp(aGraph,aGraph.numVertices-1,v)



def sp_cycle_dp(graph,k,v):
    if v.distance.has_key((k,v)):
        return
    v.setDistance(k,sys.maxint)
    v.setPred(k,None)
    for w in v.getConnection():
        new_dist=v.getDistance(k)+v.getWeight(w)
        if new_dist<w.getDistance(k):
            w.setDistance(k,new_dist)
            w.setPred(k,v)


g=DFSGraph()
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
Shortest_path_cyclic(g,g.getVertex(0))