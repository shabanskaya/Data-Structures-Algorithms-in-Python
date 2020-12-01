a = int(input())
maxi = a
count = 1
while a != 0:
    if a > maxi:
        count += 1
        maxi = a
    a = int(input())

print(count)        
