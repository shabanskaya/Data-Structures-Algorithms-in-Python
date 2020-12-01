
n, s = list(map(int, input().split()))
a = []
g = [[] for i in range(n)]
for i in range(n):
    a.append(list(map(int, input().split())))
    for k in range(n):
        if a[i][k] == 1:
            g[i].append(k)
            g[k].append(i)

d = []

Visited = [False] * (n)
def DFS(start):
    Visited[start] = True
    for v in g[start]:
        if not Visited[v]:
            DFS(v)
#ncomp = 0
if not Visited[s]:
    DFS(s)
    
summ = -1
for i in range(n):
    if Visited[i]:
        summ+=1
print( summ )
