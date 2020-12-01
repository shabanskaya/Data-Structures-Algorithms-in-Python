def plo(a, b, c, d):
    return abs((a*d - b*c)/2)

def area(z):
    x0 = z[0][0]
    y0 = z[0][1]
    summ = 0
    n = len(z)
    for i in range(1, n-1):
        a = z[i][0] - x0
        b = z[i][1] - y0
        c = z[i+1][0] - x0
        d = z[i+1][1] - y0
        summ += (plo(a, b, c, d))
    return round(summ, 5)

z = []

while True:
    s = input()
    if s == 'end':
        break
    if s == 'area':
        print(area(z))
    else:
        tmp = s.split()
        pos = int(tmp[1])
        x = float(tmp[2])
        y = float(tmp[3])
        z.insert(pos, [x, y])