n = int(input())
a = [[0, 0, 0] for c in range(n)]
for i in range(n):
    a[i][0] = int(input())
    a[i][1] = int(input())
    a[i][2] = int(input())
m = int(input())
doski = [0 for c in range(m)]
for ii in range(m):
    doski[ii] = int(input())
for ii in range(m):
    for i in range(n-1, -1, -1):
        if a[i][0] <= doski[ii] and a[i][1] >= doski[ii]:
            print(a[i][2], end = ' ')
            break
    else:
        print(0)