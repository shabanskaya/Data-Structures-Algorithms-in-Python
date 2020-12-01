dano = list(map(int, input().split()))
n = dano.pop(0)
m = dano.pop(0)

a = [[float('inf')]*n*2 for _ in range(n*2)]
    
w = [[] for _ in range(2*n)]

for i in range(m):
        k, t, we = list(map(int, input().split()))
        a[k][t+n] = we
        a[t][k+n] = we
        a[k+n][t] = we
        a[t+n][k] = we
        
        w[k].append(t+n)
        w[t].append(k+n)
        w[k+n].append(t)
        w[t+n].append(k)


def poi(start, f):    
    INF = float("inf")
    dist = [INF] * n*2
    dist[start] = 0
    prev = [None] * n*2
    used = [False] * n*2
    min_dist = 0
    min_vertex = start
    while min_dist < INF:
       i = min_vertex
       used[i] = True
       for j in w[i]:
           changed = False
           if dist[i] + a[i][j] < dist[j]:
               dist[j] = dist[i] + a[i][j] 
               prev[j] = i
       min_dist = INF
       for i in range(2*n): 
           if not used[i] and dist[i] < min_dist: 
               min_dist = dist[i] 
               min_vertex = i
    
    path = []
    while f is not None:
        path.append(f) 
        f = prev[f] 
    path = path[::-1]
    return path

k1 = int(input())
b = []
for i in range(k1):
    k, t = list(map(int, input().split()))
    b.append([k, t])

for i in range(k1):
    rasst = poi(b[i][0], b[i][1])
    if len(rasst) == 0:
        print(-1)
    else:
        for k in range(len(rasst)):
            rasst[k] = rasst[k]%n
        print(*rasst)
        
