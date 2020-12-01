a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])

n = len(a)
for i in range(n):
    m = a[i]
    k = i
    for ii in range(i, n):
        if a[ii] < m:
            m = a[ii]
            k = ii
    if a[i] != a[k]:
        a[i], a[k] = a[k], a[i]
        print(*a)