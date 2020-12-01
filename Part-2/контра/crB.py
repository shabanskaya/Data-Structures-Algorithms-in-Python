n = int(input())
a = list(map(int, input().split()))
z = 0
for i in range(n):
    x = 2*i+1
    y = 2*i+2
    if x < n:
        if a[i] < a[x]:
            z = 1
    if y < n:
        if a[i] < a[y]:
            z = 1

if z == 1:
    print('NO')
else:
    print('YES')