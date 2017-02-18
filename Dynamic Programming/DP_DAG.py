# It is of order O(V+E) and it is used for a acyclic graphs

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

def Shortest_path(aGraph,s):
    aGraph.dfs()
    order=aGraph.topologicalSort()
    s.setDistance(0)
    for vertex in order:
        for w in vertex.getConnection():
            new_dist=vertex.getDistance()+vertex.getWeight(w)
            if new_dist<w.getDistance():
                w.setDistance(new_dist)
                w.setPred(vertex)
def backtrace(g,start,end):
    path=[]
    path.append(end.getId())
    while path[-1] != start.getId():
        path.append(g.getVertex(path[-1]).parent.getId())
    path.reverse()
    return path

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
Shortest_path(g,g.getVertex(0))
print backtrace(g,g.getVertex(0),g.getVertex(3))
