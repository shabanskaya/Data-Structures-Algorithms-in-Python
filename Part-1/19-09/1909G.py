c1 = 0
c2 = 0 
c3 = 0
c4 = 0
n = int(input())
for i in range (n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x > 0:
        if y > 0:
            c1 += 1
        if y < 0:
            c4 += 1
    elif x < 0:
        if y > 0:
            c2 += 1
        if y < 0:
            c3 += 1
m = max(c1, c2, c3, c4)
if c1 == m:
    print("1", c1, sep = " ")
elif c2 == m:
    print("2", c2, sep = " ")
elif c3 == m:
    print("3", c3, sep = " ")
else:
    print("4", c4, sep = " ")
    