#Dijkstra Algorithm for weighted edges 
## Assumption: non-negative edges 
## complexcity O(VlogV+ElogV) in theory but in practical it's O(ElogV) since E is approximately V**2
## the complexicity is not dependent weights
## It can be used for cycles, but non-negative weight values.

# For negative weight cycle the algorithm is Bellman-Ford
## complexicity O(VE) i.e. more than Dijkstra algorithm

from Dijkstra_graph import Graph,Vertex,PriorityQueue

def dijkstra(aGraph,start):
    pq=PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    pq.addKeys([(v.getDistance(),v) for v in aGraph],aGraph)
    while not pq.isEmpty():
        currentVertex=pq.delMin()[1]
        for nextVertex in currentVertex.getConnection():
            newDist=currentVertex.getDistance()+currentVertex.getWeight(nextVertex)
            if newDist<nextVertex.getDistance():
                nextVertex.setDistance(newDist)
                nextVertex.setPred(currentVertex)
                pq.decreaseKey(nextVertex,newDist)
                

def backtrace(g,start,end):
    path=[]
    path.append(end.getId())
    while path[-1] != start.getId():
        path.append(g.getVertex(path[-1]).parent.getId())
    path.reverse()
    return path
"""
g=Graph()
for i in range(6):
    g.addVertex(i)

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

dijkstra(g,g.getVertex(0))
print backtrace(g,g.getVertex(0),g.getVertex(3))

"""