n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

s = 0
for i in range(n):
    for k in range(n):
        if a[i][k] != a[k][i]:
            s = 1
            break
if s == 1:
    print('NO')
else:
    print('YES')