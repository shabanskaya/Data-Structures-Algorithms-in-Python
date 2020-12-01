a = []
d = {}
n = int(input())
for i in range(n):
    a.append(list(map(int, input().split())))
    c = a[i][0]/((a[i][1]**2+a[i][0]**2)**0.5)
    s = a[i][1]/((a[i][1]**2+a[i][0]**2)**0.5)
    
    x = d.get((c, s), 0)
    if x == 0:
        d[(c, s)] = 1
    else:
        d[(c, s)] += 1

m = max(d.values())

print(m)
        