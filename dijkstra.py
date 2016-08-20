'''
from sys import stdin
n, m = stdin.readline().split()
n, m = int(n), int(m)
graph = {i:{} for i in range(n)}

# paths to themselves have zero length
for i in range(m):
    a, b, t = stdin.readline().split()
    a, b, t = int(a), int(b), int(t)
    graph[a][b] = t
    graph[b][a] = t
print graph
'''
graph = {0:{1:1,2:2,3:3}, 1:{3:2, 2:2}, 2:{1:3},3:{0:2}}

from heapq import heappush, heappop
def Dijkstra(graph, start):
    A = [None] * len(graph)
    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        print path_len, v,queue
        if A[v] is None: # v is unvisited
            A[v] = path_len
            for w, edge_len in graph[v].items():
                if A[w] is None:
                    heappush(queue, (path_len + edge_len, w))

    # to give same result as original, assign zero distance to unreachable vertices             
    return [0 if x is None else x for x in A] 


A = Dijkstra(graph, 0)
B = Dijkstra(graph, 1)
print A,B
