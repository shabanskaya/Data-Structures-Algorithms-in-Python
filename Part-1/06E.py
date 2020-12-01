a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])

n = len(a)
c = [0 for i in range(10)]

for i in range(n):
    c[a[i]] += 1
    print(*c)

s = []
for i in range(10):
    while c[i] != 0:
        c[i] -= 1
        s.append(i)
print(*s)