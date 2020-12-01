a = int(input())
m = a
while a != 0:
    b = int(input())
    if b > m and b != 0:
        m = b
    a = b
print(m)