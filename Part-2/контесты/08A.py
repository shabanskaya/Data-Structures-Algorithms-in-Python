
n, m, x, y = list(map(int, input().split()))
a = [[] for i in range(n)]

for i in range(m):
    v1, v2 = list(map(int, input().split()))
    a[v1].append(v2)
    a[v2].append(v1)

d = [-1]*n
d[x] = 0
cur = [[] for i in range(n)]
cur[0].append(x)

def poi():
    if x == y:
        return 0
    for i in range(n-1):
        for elem in cur[i]:
            for k in range(len(a[elem])):
                if a[elem][k] not in cur[i+1]:
                    cur[i+1].append(a[elem][k])
                if a[elem][k] == y:
                    return i+1

#for i in range(n):
 #   if y in cur[i]:
  #      ind = i
   #     break
print(poi())
    