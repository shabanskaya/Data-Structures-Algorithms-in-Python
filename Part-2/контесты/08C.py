n, m = list(map(int, input().split()))
a = [[] for i in range(n)]

for i in range(m):
    v1, v2 = list(map(int, input().split()))
    a[v1].append(v2)



cic = []
puti = []

def der(x):
    d = [True]*n
    d[x] = False
    cur = [[] for i in range(n)]
    cur[0].append([-1, x])
    #s = 1
    for i in range(n-1):
        for elem in cur[i]:
            for k in range(len(a[elem[1]])):
                if d[a[elem[1]][k]] or a[elem[1]][k] == x:
                    cur[i+1].append([elem[1], a[elem[1]][k]])
                    d[a[elem[1]][k]] = False
                
                if a[elem[1]][k] == x:
                    cic.append(i+1)
                    lst = []
                    tmp = x
                    for l in range(i+1, 0, -1):
                        for v in cur[l]:
                            if v[1] == tmp:
                                tmp = v[0]
                                lst.append(v[0])
                    puti.append(lst[::-1])
                    return
                
                elif True not in d:
                    cic.append(2*n)
                    puti.append([2*n])
                    return
    cic.append(2*n)
    puti.append([2*n])
    return
          
for i in range(n):
    der(i)

if min(cic) == 2*n:
    print("NO CYCLES")
else:
    print(*puti[cic.index(min(cic))])
