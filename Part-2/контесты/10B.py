n, m = list(map(int, input().split()))
d = [[] for i in range(n)]
for i in range(m):
    a, b = list(map(int, input().split()))
    if b-1 not in d[a-1]:
        d[a-1].append(b-1)

color = [ 0 ] * n
cycleFound = 0

def dfs ( start ) :
    color[start] = 1
    for v in d[start]:
        if color[v] == 0 :
            dfs( v )
        elif color[v] == 1 :
            cycleFound = 1
    color[start] = 2

for i in range(n) :
    if color[i] == 0 :
        dfs(i)

if cycleFound==1:
    print("No")
else:
    print("Yes")