a = int(input())
c = 0
s = 0
while a != 0:
    c += 1
    s += a
    a = int(input())
print(round((s/c), 2))