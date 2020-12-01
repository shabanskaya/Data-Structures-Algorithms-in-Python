a = input().split()
b = []
for i in range(len(a)):
    if len(a[i]) >= 5:
        x = 0
        for s in range(len(a[i])):
            x += ord(a[i][s:s+1])
        b.append(x)
print(*b)