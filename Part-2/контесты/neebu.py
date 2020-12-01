from collections import deque

n, m = map(int, input().split())
g = {v : {} for v in range(n)}


def add_edge(g, v1, v2, w):
    g[v1][v2] = w
        

def create_graph():
    for _ in range(m):
        v1, v2, w = map(int, input().split())
        add_edge(g, v1, v2, w)
        add_edge(g, v2, v1, w)
    return g


def poi(graph, start):
    queue = deque([start])
    distances = dict()
    distances[start] = 0
    while queue:
        cur_v = queue.popleft()
        for neigh_v in graph[cur_v]:
            if (neigh_v not in distances
                or 
                distances[cur_v] + graph[cur_v][neigh_v] < distances[neigh_v]
               ):
                distances[neigh_v] = distances[cur_v] + graph[cur_v][neigh_v]
                queue.append(neigh_v)
    return distances


create_graph()