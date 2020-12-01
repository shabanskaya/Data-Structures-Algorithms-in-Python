a = int(input())
m = a
c = 1
mini = a
maxi = a
while a!=0:
    c += 1
    x = int(input())
    if x < mini and x != 0:
        mini = x
    if x > maxi and x != 0:
        maxi = x
    m += x
    a = x
nado = (mini+maxi)*c/2
print(int(nado - m))