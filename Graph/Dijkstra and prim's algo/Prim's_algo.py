# This algo is based on greedy algorithm and used in networking
# It is based majorily on unflooding technique used in broadcasting
# You just select the eedge with the lowest weight and send your message to the vertex connecting the least weight edge

from Dijkstra_graph import PriorityQueue, Graph, Vertex

def prim(g,start):
    pq=PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in g])
    pq.addKeys([(v.getDistance(),v) for v in g],g)
    while not pq.isEmpty():
        currentVertex=pq.delMin()[1]
        for nextVertex in currentVertex.getConnection():
            newCost=currentVertex.getWeight(nextVertex)
            if nextVertex in pq.key and newCost<nextVertex.getDistance():
                nextVertex.setDistance(newCost+currentVertex.getDistance())
                nextVertex.setPred(currentVertex)
                pq.decreaseKey(nextVertex,newCost)

g=Graph()
g.addEdge('A','B',2)
g.addEdge('A','C',3)
g.addEdge('B','C',1)
g.addEdge('B','E',4)
g.addEdge('B','D',1)
g.addEdge('C','F',5)
g.addEdge('D','E',1)
g.addEdge('E','F',1)
g.addEdge('F','G',1)
prim(g,g.getVertex('A'))
