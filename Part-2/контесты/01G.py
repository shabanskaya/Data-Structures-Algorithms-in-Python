def month(x):
    if x == 'January':
        return 1
    if x == 'February':
        return 2
    if x == 'March':
        return 3
    if x == 'April':
        return 4
    if x == 'May':
        return 5
    if x == 'June':
        return 6
    if x == 'July':
        return 7
    if x == 'August':
        return 8
    if x == 'September':
        return 9
    if x == 'October':
        return 10
    if x == 'November':
        return 11
    if x == 'December':
        return 12

def chas(x):
    s = ''
    x = list(x)
    i = 0
    while x[i] != ':':
        s+=x[i]
        i+=1
    return int(s)

def minut(x):
    s = ''
    x = list(x)
    i = len(x) - 1
    while x[i] != ':':
        s = x[i] + s
        i-=1
    return int(s)

def comp(x, y):
    if int(x[2]) < int(y[2]):
        return True
    if int(x[2]) == int(y[2]):
        if month(x[1]) < month(y[1]):
            return True
        if month(x[1]) == month(y[1]):
            if int(x[0]) < int(y[0]):
                return True
            if int(x[0]) == int(y[0]):
                if chas(x[3]) < chas(y[3]):
                    return True
                if chas(x[3]) == chas(y[3]):
                    if minut(x[3]) < minut(y[3]):
                        return True
                    if minut(x[3]) == minut(y[3]):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def sort(s, comp):
    n = len(s)
    for _ in range(n):
        for i in range(n-1):
            if comp(s[i], s[i+1]):
                e = 0
            else:
                s[i], s[i+1] = s[i+1], s[i]
    return s




n = int(input())
s = [[] for i in range(n)]
for i in range(n):
    s[i] = input().split()

s = sort(s, comp)
for i in range(n):
    print(*s[i])