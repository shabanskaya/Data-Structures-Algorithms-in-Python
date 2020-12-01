def vektpr(a, b, c, d):
    return(a*d - b*c)

def sign(x):
    if x > 0.000001:
        return 1
    if x < -0.000001:
        return -1
    return 0

z = []
n = int(input())
for i in range(n):
    z.append(list(map(float, input().split())))
    
x0, y0 = list(map(float, input().split()))
x = []

for i in range(n-1):
    a = z[i][0] - x0
    b = z[i][1] - y0
    c = z[i+1][0] - x0
    d = z[i+1][1] - y0
    k = vektpr(a, b, c, d)
    x.append(sign(k))
    
a = z[n-1][0] - x0
b = z[n-1][1] - y0
c = z[0][0] - x0
d = z[0][1] - y0
k = vektpr(a, b, c, d)
x.append(sign(k))

for i in range(len(x)):
    if x[i] == 0:
        print("YES")
        break
    if x[i] == -1:
        print("NO")
        break
else:
    print('YES')