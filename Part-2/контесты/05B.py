def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

a = input().split()
for i in range(len(a)):
    if isfloat(a[i]):
        a[i] = float(a[i])
        
c = 0
i = 0
while len(a) > i:
    if isfloat(a[i]):
        c = a[i]
        i+=1
    elif a[i] == "#":
        a[i] = 0
        for h in range(i):
            znach = a.pop(0)
            a[i-h-1] += znach
        i = 1
        c = a[0]
    elif a[i] == "%":
        if i >=2:
            proc = a.pop(i-1)
            dig = a.pop(i-2)
            i = i - 2
            a[i] = (proc / 100) * dig
            c = a[i]
            i+=1
        else:
            c = 0.0
            break
    #print(a, i, c)

print(c)
    
        