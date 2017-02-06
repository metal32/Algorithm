from Graph import Graph
class DFSgraph(Graph):
    def __init__(self):
        Graph.__init__(self)
        self.time=0
        self.order=[]
        self.final=[]
        
    def dfs(self,alist):
        for a in alist:
            aVertex=self.getVertex(a)
            aVertex.setColor("white")
        for a in alist:
            aVertex=self.getVertex(a)
            if aVertex.getColor() == 'white':
                self.final.append(aVertex.id)
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