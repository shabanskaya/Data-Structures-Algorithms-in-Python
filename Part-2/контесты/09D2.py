from collections import deque

n, m = map(int, input().split())

g = dict() 


        

def make():
    for i in range(m):
        u, v, w = map(int, input().split())
        ad(g, u, v, w)
        ad(g, v, u, w)

def ad(g, v1, v2, w):
    if (v1, 0) not in g:
        g[(v1, 0)] = {(v2, 1) : w}
        g[(v1, 1)] = {(v2, 0) : w}
    else:
        g[(v1, 0)][(v2, 1)] = w
        g[(v1, 1)][(v2, 0)] = w
        

def poi(g, s):
    q = deque([s])
    d = dict()
    d[s] = 0
    while q:
        cur = q.popleft()
        for nei in g[cur]:
            if (nei not in d or d[cur] + g[cur][nei] < d[nei]):
                d[nei] = g[cur][nei]+d[cur]
                q.append(nei)
    return d



def path(g, s, f):
    d = poi(g, s)
    if f not in d:
        return [(-1, 0)]
    
    mpath = [f]
    cur = f
    while cur != s:
        for nei in g[cur]:
            if d[cur] == d[nei] + g[nei][cur]:
                mpath.append(nei)
                cur = nei
                break
    return mpath[::-1]

make()

k = int(input())
d = []

for i in range(k):
    d.append(tuple(map(int, input().split())))

for i in range(k):
    rasst = path(g, (d[i][0], 0), (d[i][1], 0))
    print(*[d[0] for d in rasst])