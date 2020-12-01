n, m = map(int, input().split())
g = {v : set() for v in range(n)}

for i in range(m):
    x, y = map(int, input().split())
    g[x].add(y)

def dfs_stack(v, g, colour, stack):
    colour[v] = 1
    for u in g[v]:
        if colour[u] == 0:
            stack[u] = v
            if dfs_stack(u, g, colour, stack):
                return True 
        elif colour[u] == 1:
            lst.append(u)
            lst.append(v)
            return True
    colour[v] = 2
    return False

stack = [-1] * n
colour = [0] * n  
lst = []  
cyc = []
   
for v in g:
    if dfs_stack(v, g, colour, stack):
        break  
if lst: 
    t = lst[1]
    while t != lst[0]:
        cyc.append(t)
        t = stack[t]
    cyc.append(lst[0])
    cy = cyc[len(cyc)-1:-1:-1]
    print(*cy)

else:
    print('YES')