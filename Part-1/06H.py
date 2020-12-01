def sorti(a):
    n = len(a)
    for i in range(1, n):
        for s in range(i-1, -1, -1):
            if a[s+1] < a[s]:
                a.insert(s, a.pop(s+1))
    return a

def chet(x):
    return x%2 == 0

n = int(input())
a = []
c = []
m = []
for i in range(n):
    a.append(int(input()))
    if chet(a[i]):
        c.append(a[i])
        m.append(i)

c = sorti(c)
for i in range(len(c)):
    a.insert(m[i], c[i])
    a.pop(m[i]+1)


print(*a)       