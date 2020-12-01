n, m = list(map(int, input().split()))
a = [[] for i in range(n)]

for i in range(m):
    v1, v2 = list(map(int, input().split()))
    a[v1].append(v2)
    a[v2].append(v1)

cur = [[] for i in range(n)]
cur[0].append([-1, v2])

d = [True]*n
d[v2] = False

def der():
    #s = 1
    for i in range(n-1):
        for elem in cur[i]:
            for k in range(len(a[elem[1]])):
                if d[a[elem[1]][k]]:
                    cur[i+1].append([elem[1], a[elem[1]][k]])
                    d[a[elem[1]][k]] = False
                    #s+=1
                #if s == n:
                if True not in d:
                    return
der()
            
for i in range(1, n):
    for elem in cur[i]:
        print(*elem)

                #if [elem[1], a[elem[1]][k]] not in cur[i+1]:
