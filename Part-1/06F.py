a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])

n = len(a)
b = []
for i in range(10):
    b.append([])

m = max(a)
r = 1
while m//10 != 0:
    m = m//10
    r+=1

for i in range(r):
    for s in range(n):
        b[(a[s] // (10**i)) % 10].append(a[s])
        k = 0
    for s in range(10):
        for ss in range(len(b[s])):
            a[k] = b[s][ss]
            k += 1
    for i in range(10):
        b[i].clear()
    print(*a)