n = int(input())

a = [[1, 1, 0], [1, 1, 2]]
for i in range(n-2):
    a.append([0, 0, 0])
    
for i in range(2, n):
    a[i][0] = a[i-1][1]
    a[i][1] = a[i-1][2]
    a[i][2] = a[i-1][0]+a[i-1][2]+a[i-1][1]

print(a[n-1][0]+a[n-1][1]+a[n-1][2])