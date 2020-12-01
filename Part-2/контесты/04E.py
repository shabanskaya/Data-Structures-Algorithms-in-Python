a1, b1, c1 = list(map(int, input().split()))
a2, b2, c2 = list(map(int, input().split()))

def peres(a1, b1, c1,a2, b2, c2):
    if a1*b2 == a2*b1:
        if a1*c2 == a2*c1:
            return [0, round(c2/b2)]
        return ['NO']
    x = (b1*c2 - b2* c1)/(a1*b2 - b1*a2)
    y = -((c2+(a2*x))/b2)
    return [round(x), round(y)]

print(*peres(a1, b1, c1,a2, b2, c2))