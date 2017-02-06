## Strongly Connected Components algorithm of order O(V+E) using Kosaraju’s algorithm

from DFS_Graph import DFSGraph
from DFSGraph_2 import DFSgraph

g=DFSGraph()
g.addEdge('A','B')
g.addEdge('B','C')
g.addEdge('B','E')
g.addEdge('C','C')
g.addEdge('C','F')
g.addEdge('D','B')
g.addEdge('D','G')
g.addEdge('E','A')
g.addEdge('E','D')
g.addEdge('F','H')
g.addEdge('G','E')
g.addEdge('H','I')
g.addEdge('I','F')
g.dfs()

# vertex with decreasing finish time
alist=list(g.topologicalSort())

# Create a transpose graph and do the dfs with the vertex ordered above

gt=DFSgraph()
gt.addEdge('B','A')
gt.addEdge('C','B')
gt.addEdge('E','B')
gt.addEdge('C','C')
gt.addEdge('F','C')
gt.addEdge('B','D')
gt.addEdge('G','D')
gt.addEdge('A','E')
gt.addEdge('D','E')
gt.addEdge('H','F')
gt.addEdge('E','G')
gt.addEdge('I','H')
gt.addEdge('F','I')

gt.dfs(alist)

print gt.final


