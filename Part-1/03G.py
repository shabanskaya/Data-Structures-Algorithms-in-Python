a, n = input().split()
summa = 0
c = 0
while n != 'A999AA':
    a = int(a)
    if a > 60:
        n = int(n[1:4:1])
        a1 = n//100
        a2 = (n//10)%10
        a3 = n%10
        if a1 == a2:
            if a1 == a3:
                c = 1000
            else:
                c = 500
        elif a2 == a3 or a1 == a3:
            c = 500
        else:
            c = 100
        summa += c
    a, n = input().split()
print(summa)