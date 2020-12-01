n, m = map(int, input().split())
a = {v : set() for v in range(n)}
for i in range(m):
    u, v, w = map(int, input().split())
    a[u].add((v, w))
    a[v].add((u, w))
s = {0}
e = []
wei = 0
for _ in range(n-1):
    u = -1
    j = -1
    min_w = float("inf")
    for u in s:
        for v, w in a[u]:
            if v not in s and w<min_w:
                min_w = w
                i = u
                j = v
    e.append((i, j, min_w))
    wei += min_w
    s.add(j)
print(wei)
for i in range(len(e)):
    print(e[i][0], e[i][1])
