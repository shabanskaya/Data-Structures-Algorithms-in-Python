def DFS(a, start, Color, stack):
    stack.append(start)
    Color[start] = 1
    print(Color)
    for u in a[start]:
        print(u)
        print(stack)
        if Color[u] == 1:
            #print("nasheel")
            Color[u] = 2
            #print(stack)
            print(*stack)
            return
        if Color[u] == 0:
            DFS(a, u, Color, stack)
    stack = []
    #return True

n, m = list(map(int, input().split()))
a = [[] for i in range(n)]

for i in range(m):
	x, y = list(map(int, input().split()))
	a[x].append(y)

#ind = True

s = 0
for i in range(n):
    Color = [0] * (n)
    stack = []
    DFS(a, i, Color, stack)
    if 2 in Color:
        s = 1
        break

if s == 1:
    pass
else:
    print("YES")