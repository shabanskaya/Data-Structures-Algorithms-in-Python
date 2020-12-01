n = int(input())
max1 = 0
max2 = 0
min1 = 1000000
min2 = 1000000

for word in input().split():
    a = int(word)
    if a >= max1:
        max2 = max1
        max1 = a
    elif a >= max2:
        max2 = a
    if a < min1:
        min2 = min1
        min1 = a
    elif a < min2:
        min2 = a

print(min1+min2, max1+max2)