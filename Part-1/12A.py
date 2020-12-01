x, y = map(int, input().split())
a = [[0]*8 for i in range(8)]
for i in range(8):
    a[7][i] = 1
for i in range(1,8):
    for j in range(8):
        if j-1 > -1:
            a[7-i][j]+=a[7-i+1][j-1]
        if j!=7:
            a[7-i][j]+=a[7-i+1][j+1]
    
print(a[y-1][x-1])