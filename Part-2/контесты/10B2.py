n, m = map(int, input().split())

graph = {v : set() for v in range(n)}

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1-1].add(v2-1)
    
    
def dfs(v, graph, color):
    color[v] = 1  # красим вершину в серый цвет 
    for neighbour in graph[v]:
        if color[neighbour] == 0:
            if dfs(neighbour, graph, color):
                return True
        elif color[neighbour] == 1:
            loop.append(neighbour)
            loop.append(v)
            return True
    color[v] = 2
    return False


color = [0] * n
loop = []
            
for v in graph:
    if dfs(v, graph, color):
        break 

if loop:
    print("No")
else:
    print('Yes')