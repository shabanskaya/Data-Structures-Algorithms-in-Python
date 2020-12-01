n = int(input())
c2 = 0
c5 = 0
for i in range (2, n+1):
    while i%5 == 0:
        c5 += 1
        i /= 5
    while i%2 == 0:
        c2 += 1
        i /= 2
print(min(c2, c5))