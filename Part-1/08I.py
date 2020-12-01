def summ(L):
    the = 0
    for i in L:
        the = the + i
    return the

n =int(input())

a = [[i] for i in range(n)]

c = input()
while c != '#':
    v, w = map(int, c.split())
    a[v].append(w)
    c = input()
for i in range(n):
    a[i].insert(0, summ(a[i]))
a.sort(reverse = True)

for i in range(n):
    x = a[i].pop(0)
    x = a[i].pop(0)
    a[i].sort(reverse = True)
    print(*a[i], end = ' ')
        