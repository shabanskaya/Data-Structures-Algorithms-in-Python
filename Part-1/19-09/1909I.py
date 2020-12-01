a = int(input())
c1 = int(input())
c2 = int(input())
c3 = int(input())
c4 = int(input())
c5 = int(input())
m = a
while c5 != 0:
    b = int(input())
    if a > m and a != 0:
        m = a
    a = c1
    c1 = c2
    c2 = c3
    c3 = c4
    c4 = c5
    c5 = b
print (m)    