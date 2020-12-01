a = list(map(int, input().split()))
x0, y0 = list(map(int, input().split()))

def smen(x, x0):
    return (2*x0 - x)

for i in range(0, 6, 2):
    a[i] = smen(a[i], x0)
    a[i+1] = smen(a[i+1], y0)

print(*a)