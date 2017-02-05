from Graph import Graph, Vertex

def BFS(start):
    frontier=[start]
    i=1
    while frontier:
        next=[]
        for n in frontier:
            for v in n.getConnection():
                if v not in start.level:
                    start.level[v]=i
                    v.parent=n
                    next.append(v)
        frontier=next
        i+=1

def backtrace(g,start,end):
    path=[]
    path.append(end.getId())
    while path[-1] != start.getId():
        path.append(g.getVertex(path[-1]).parent.getId())
    path.reverse()
    return path

g=Graph()
for i in range(6):
    g.addVertex(i)

g.addEdge(0,1)
g.addEdge(0,5)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,0)
g.addEdge(5,4)
g.addEdge(5,2)

start=g.getVertex(0)
end=g.getVertex(4)
BFS(start)



print backtrace(g,start,end)