a = input()
n = len(a)
a = int(a)
summa = 0
for i in range(n):
    base = (-10)**i
    number = a // (10**(i)) % 10
    summa += base * number
print(summa)