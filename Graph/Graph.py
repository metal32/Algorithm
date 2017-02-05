class Vertex:
    def __init__(self,key):
        self.id=key
        self.connectedTo={}
        self.level={self:0}
        self.parent=None

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr]=weight

    def __str__(self):
        return str(self.id)+' connected to '+str([x.id for x in self.connectedTo])

    def getConnection(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList={}
        self.numVertices=0

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

g=Graph()
#for i in range(6):
#    g.addVertex(i)

#g.addEdge(0,1,5)
#g.addEdge(0,5,2)
#g.addEdge(1,2,4)
#g.addEdge(2,3,9)
#g.addEdge(3,4,7)
#g.addEdge(3,5,3)
#g.addEdge(4,0,1)
#g.addEdge(5,4,8)
#g.addEdge(5,2,1)

#for v in g:
#    for w in v.getConnection():
#        print '( {}, {} )'.format(v.getId(),w.getId())