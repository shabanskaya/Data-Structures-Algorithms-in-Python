n, m = list(map(int, input().split()))

a = []

for i in range(m):
    a.append(list(map(int, input().split())))
    
V = [[] for i in range(n)]
for i in range(m):
    V[a[i][0]].append(a[i][1])


acicle = True
l = []

def DFS(start, stack, l, vis, acicle):
    vis.add(start)
    stack.append(start)
    #print(vis, stack)
    for u in V[start]:
        #print(u)
        if u in stack:
            x = stack.index(u)
            #print(x, '9939393')
            for i in range(x, len(stack)):
                l.append(stack[i])
            #print(*l)
            acicle = False
            break
        elif u not in vis:
            DFS(u, stack, l, vis, acicle)
        else:
            stack = []

vis = set()            
stack =[]

for i in range(n):
    if i not in vis:
        DFS(i, stack, l, vis, acicle)

if l == []:
    print('YES')
else:
    print(*l)