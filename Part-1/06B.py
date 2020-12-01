a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])

n = len(a)
for i in range(1, n):
    for s in range(i-1, -1, -1):
        if a[s+1] < a[s]:
            a.insert(s, a.pop(s+1))
            print(*a)
            