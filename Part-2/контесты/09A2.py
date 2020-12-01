n, m, start, f = list(map(int, input().split()))

a = [[float('inf')]*n for _ in range(n)]

w = [[] for _ in range(n)]

for i in range(m):
    k, t, we = list(map(int, input().split()))
    a[k][t] = we
    a[t][k] = we
    w[k].append(t)
    w[t].append(k)
    

INF = float("inf")
dist = [INF] * n
dist[start] = 0
prev = [None] * n
used = [False] * n
min_dist = 0
min_vertex = start
while min_dist < INF:
   i = min_vertex
   used[i] = True
   for j in w[i]:
       if dist[i] + a[i][j] < dist[j]:
           dist[j] = dist[i] + a[i][j] 
           prev[j] = i
   min_dist = INF
   for i in range(n): 
       if not used[i] and dist[i] < min_dist: 
           min_dist = dist[i] 
           min_vertex = i

path = []
#fin = f
while f is not None:
    path.append(f) 
    f = prev[f] 
path = path[::-1]
#path.append(fin)
print(*path)