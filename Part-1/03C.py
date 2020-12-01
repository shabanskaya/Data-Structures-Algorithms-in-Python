a = int(input())
count = 0
summa = 0
summa_sq = 0

while a != 0:
    count += 1
    summa += a
    summa_sq += a**2
    a = int(input())

m = summa/count
m = round(m, 3)

d = (summa_sq/count) - (summa/count)**2
d = round(d, 3)

print(m, d)