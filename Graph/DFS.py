#An edge(u,v) is a forwardedge, if v is finished and starttime[u]<starttime[v].
#An edge(u,v) is a crossedge, if v is finished and starttime[u]>starttime[v].
class DFSResult(object):
    def __init__(self):
        self.parent={}
        self.start_time={}
        self.finish_time={}
        self.edges={} #Edge classification in directed graph
        self.order=[]
        self.t=0
def dfs(g):
    # g is the adjacency list
    results=DFSResult()
    # iterate through all the vertices
    for vertex in g:
        if vertex not in results.parent:
            dfs_visits(g,vertex,results)
    return results

def dfs_visits(g,v,results,parent=None):
    results.parent[v]=parent
    results.t+=1
    results.start_time[v]=results.t
    if parent:
        results.edges[(parent,v)]='tree'
    for n in g.get(v,[]):
        # if n is not visited
        if n not in results.parent:
            dfs_visits(g,n,results,v)
        elif n not in results.finish_time:
            results.edges[(v,n)]='back'
        elif results.start_time[v]<results.start_time[n]:
            results.edges[(v,n)]='forward'
        else:
            results.edges[(v,n)]='cross'
    results.t+=1
    results.finish_time[v]=results.t
    results.order.append(v)

def topological_sort(g):
    dfs_result=dfs(g)
    dfs_result.order.reverse()
    return dfs_result.order
graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
print dfs(graph).edges
print dfs(graph).start_time
print dfs(graph).finish_time
print dfs(graph).order
print topological_sort(graph)

