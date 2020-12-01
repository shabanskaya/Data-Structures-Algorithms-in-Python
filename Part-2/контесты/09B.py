n, m, s = map(int, input().split())

edges = []

for i in range(m):
    edges.append(list(map(int, input().split())))

d = [10**10] * n
d[s] = 0

for i in range(n-1):
    for u, v, w in edges:
        if (d[u] != 10**10 and d[v] > d[u] + w):
            d[v] = d[u] + w
for u, v, w in edges:
    if (d[u] != 10**10 
        and
        d[v] > d[u] + w
       ):
        d[v] = -10**10
        
for i in range(len(d)):
    if (abs(d[i]) >= 10**10):
        d[i] = 'UDF'
        
print(*d)