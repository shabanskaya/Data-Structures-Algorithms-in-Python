b = 91
M = 100

def code(c):
    return ord(c)

def poly_hash (s):
    h=[0]
    for c in s:
        h.append((h[-1]*b + code(c))%M) 
    return h

a = []

t = input()
s = input()

n = len(t)
m = len(s)
s = poly_hash(s)
t = poly_hash(t)[-1]
for i in range(m - n + 1):
    if t == ((s[i + n] - s[i] * b**n) % M):
        a.append(i)

if len(a) == 0:
    print(-1)
else:
    print(*a)
