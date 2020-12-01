n, m = list(map(int, input().split()))
g = [[] for i in range(n)]
for i in range(m):
    k , kk, w = list(map(int, input().split()))
    g[kk].append([k, w])
    g[k].append([kk, w])

d = []
m = []
Visited = [False] * (n)

def DFS(start):
    m.append(start)
    Visited[start] = True
    for v , w in g[start]:
        if not Visited[v]:
            DFS(v)

ncomp = 0
comp = []
for i in range(0, n): 
    if not Visited[i]:
        ncomp +=1
        DFS(i)
        comp.append(m)
        m = []

wii = []

for i in range(ncomp):
    x = 0
    for k in range(len(comp[i])):
        for h in range( len( g[comp[i][k]] ) ):
            x+=(g[comp[i][k]][h][1])
    wii.append(x//2)
    
wii.sort()
for i in range(len(wii)):
    print(wii[i])