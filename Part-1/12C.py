def nom(s):
    l = 'abcdefgh'
    return l.index(s)

a = [[0]*8 for i in range(8)]
n = int(input())
for i in range(n):
    x, y = list(input())
    x = nom(x)
    y = int(y) - 1
    a[y][x] = -1

x, y = list(input())
x = nom(x)
y = (int(y) - 1) #пешка в а у х 

for i in range(8):
    if a[0][i] == 0:
        a[0][i] = 1
for i in range(1, 7):
    for j in range(8):
        if a[i][j] == -1:
            if j!=0 and a[i-1][j-1]!=-1:
                a[i][j]+=a[i-1][j-1]
            if j!=7 and a[i-1][j-1]!=-1:
                a[i][j]+=a[i-1][j+1]
            if a[i][j] != -1:
                a[i][j]+=1
        if a[i][j] == 0 and a[i-1][j] != -1:
            a[i][j]+=a[i-1][j]
print(a[y][x])
            
            

