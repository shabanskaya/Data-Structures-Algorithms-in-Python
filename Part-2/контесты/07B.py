n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    for k in range(n):
        if a[i][k] != 0:
            print(i, k, a[i][k])
            