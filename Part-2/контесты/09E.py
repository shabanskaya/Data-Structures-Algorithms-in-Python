dano = list(map(int, input().split()))
n = dano.pop(0)
m = dano.pop(0)

#a = [[] for _ in range(n)]
edges = []
for i in range(m):
    k, t, w = list(map(int, input().split()))
    #a[k].append([t, w])
    #a[t].append([k, w])
    edges.append([t, k, w])
    edges.append([k, t, w])



def poi(s):
    d = [float("inf")] * n
    d[s] = 0
    for _ in range(1, n):
        changed = False
        for u, v, w in edges:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                changed = True
        if not changed:
            break
    return d

r = [[] for i in range(n)]

g = len(dano)

for i in range(g):
    ss = poi(dano[i])
    for k in range(n):
        r[k].append(ss[k])   #в r списки расстояний от каждого до главных

for i in range(n):
    if i in dano:
        print(i)
    else:
        rasst = min(r[i])
        if rasst == float("inf"):
            print(-1)
        else:
            print(dano[r[i].index(rasst)])
        

"""
for i in range(n):
    if i in dano:
        print(i)
    else:
        d = poi(i)
        p = []
        for k in range(n):
            if k in dano:
                p.append(d[k])
                
        rasst = min(p)
        if rasst == float("inf"):
            print(-1)
        else:
            print(dano[p.index(rasst)])
"""