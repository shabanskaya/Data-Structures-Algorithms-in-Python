n, m = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))

d = [[] for i in range(n)]
for i in range(n-1):
    d[a[i][0]].append(a[i][1])
    d[a[i][1]].append(a[i][0])



def dfs(u, visited):              
    visitedVertices = 1
    visited[u] = True #                          // помечаем вершину как пройденную
    for v in d[u]: #uv ∈ E                               // проходим по смежным с u вершинам
        if not visited[v]: #                       // проверяем, не находились ли мы ранее в выбранной вершине
            visitedVertices += dfs(v, visited)
    return visitedVertices
            
visited = [0]*n
zz = 0
e = m

for i in range(n-1, m):
    visited = [False]*n
    x = dfs(0, visited)
    if x == n:
        zz = 1
        e = i 
        break
    else:
        d[a[i][0]].append(a[i][1])
        d[a[i][1]].append(a[i][0])
print(e)