from Graph import Graph
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
        self.order.append(aVertex.id)

    def topologicalSort(self):
        return self.order[::-1]

        
g=DFSGraph()
g.addEdge('A','B')
g.addEdge('A','D')
g.addEdge('B','C')
g.addEdge('B','D')
g.addEdge('D','E')
g.addEdge('E','B')
g.addEdge('E','F')
g.addEdge('F','C')

g.dfs()

print g.topologicalSort()