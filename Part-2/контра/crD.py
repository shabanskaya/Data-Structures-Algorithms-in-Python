n = int(input())
a = []
for i in range(n):
    x = input()
    if x == '-':
        q = a.pop(0)
        print(q)
    else:
        z, m = x.split()
        if z == '+':
            a.append(m)
        else:
            a.insert((len(a)-1)//2+1, m)