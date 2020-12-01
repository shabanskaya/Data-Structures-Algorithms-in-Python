from collections import deque
import itertools

n, m = map(int, input().split())

a = []

for i in range(n):
    a.append(list(map(int, input().split())))

g = {v : set() for v in itertools.product(range(n), range(m))}

for i in range(n):
    for j in range(m):
        if i-1 >= 0:
            g[(i, j)].add((i-1, j))
        if i+1 < n:
            g[(i, j)].add((i+1, j))
        if j-1 >= 0:
            g[(i, j)].add((i, j-1))
        if j+1 < m:
            g[(i, j)].add((i, j+1))

d = [[None for i in range(m)] for t in range(n)]


def poi(v):
    d[v[0]][v[1]] = 0
    que = deque([v])
    while que:
        cur = que.popleft()
        for nei_v in g[cur]:
            if (d[nei_v[0]][nei_v[1]] is None or d[cur[0]][cur[1]] + 1 < d[nei_v[0]][nei_v[1]]): 
                d[nei_v[0]][nei_v[1]] = d[cur[0]][cur[1]] + 1
                que.append(nei_v)

for v in g:
    if a[v[0]][v[1]] == 1:
        poi(v)
            
for i in range(n):
    print(*d[i])