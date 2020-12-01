def ras(x1, y1, x2, y2):
    r = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return r

def dogon(a, n, x1, y1, x2, y2):
    for i in range(n):
        x3 = a[i][0]
        y3 = a[i][1]
        r1 = ras(x1, y1, x3, y3)
        r2 = ras(x2, y2, x3, y3)
        if r1 * 2 < r2:
            return [i+1]
    return [-1]

x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

print(*dogon(a, n, x1, y1, x2, y2))