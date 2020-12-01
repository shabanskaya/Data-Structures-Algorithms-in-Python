def dfs(k, z, v, used, stack):
    used.add(v[k][z][0])
    stack.append(v[k][z][0])
    for i in range(len(v[k])):
        if v[k][i][1] not in used:
            dfs(v[k][i][1], i, v, used, stack)




n = int(input())
m = int(input())

v = [[] for i in range(n)]
a = []

for i in range(m):
    a.append(list(map(int, input().split())))
    
for i in range(m):
    v[a[i][0]].append(a[i])
    
used = set()
stack = []

for k in range(n):
    for z in range(len(v[i])):
        if v[k][z][0] not in used:
            dfs(k, z, v, used, stack)
        
print(used, stack)