def tr(a):
    if len(a) == 1:
        print(*a)
        return 0
    print(*a)
    x = a.pop(0)
    return tr(a)

def mass(b, a):
    if len(a) == 0:
        return 0
    x = a.pop(0)
    b.append(x)
    tr(b[:])
    return mass(b, a)

k = list(map(int, input().split()))

mass([], k)
        