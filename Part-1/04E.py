def summa_razr(i, numm):
    c = 0
    for v in range(numm):
        c+=(i//(10**v))%10
    return c

summ, numm = input().split()
summ = int(summ)
numm = int(numm)
m = 0

g = 0
for i in range(numm):
    g+=10**i
    
for i in range (g, 10**numm):
    if summa_razr(i, numm) == summ:
        print(i)
        m+=1
        break

if m == 0:
    print("impossible")