def perese(r, r1, r2):
    c = max(r, r1, r2)
    if c > (r1 + r2 + r - c):
        return False
    return True

a = input().split()
b = input().split()

x1 = int(a[0])
y1 = int(a[1])
r1 = int(a[2])
x2 = int(b[0])
y2 = int(b[1])
r2 = int(b[2])
r = ((((x1-x2)**2)+((y1-y2)**2)))**0.5

if perese(r, r1, r2):
    print('YES')
else:
    print('NO')