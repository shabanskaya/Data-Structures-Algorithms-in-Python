n = int(input())
m = int(input())
a = [[0]* m for i in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j] = int(input())
est = int(input())

for i in range(1, n):
    a[i][0]+=a[i-1][0]
for i in range(1, m):
    a[0][i]+=a[0][i-1]

for i in range(1, n):
    for j in range(1, m):
        a[i][j]+=min(a[i-1][j], a[i][j-1])

if a[n-1][m-1]>est:
    print('Impossible')
else:
    print(est - a[n-1][m-1])