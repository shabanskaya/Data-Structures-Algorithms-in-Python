n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

ist = []
sto = []
for i in range(n):
    if 1 not in a[i]:
        sto.append(i+1)
for i in range(n):
    podh = True
    for k in range(n):
        if a[k][i] == 1:
            podh = False
            break
    if podh:
        ist.append(i+1)

print(*ist)
print(*sto)
        