a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])

n = len(a)
for _ in range(n):
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            print(*a)

