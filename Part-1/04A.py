a = int(input())
sq = int(a**0.5) + 1
c = 1
for i in range (2, sq):
    if a % i == 0:
       c = 0
print(c)