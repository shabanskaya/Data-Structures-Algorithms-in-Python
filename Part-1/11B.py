a = input().split()
b = sorted(a)
c = sorted(b, key = len)
d = []
for i in range(len(c)):
    x = 0
    for s in range(len(c[i])):
        x += ord(c[i][s:s+1])
    d.append(x)
print(*d)