a = int(input())
m = a
c = 0
while a != 0:
    if a > m:
        m = a
        c = 1
    elif a == m:
        c+=1
    a = int(input())


print(c)