a = int(input())
count = 0
while a != 0:
    if a % 2 == 0:
        count += 1
    a = int(input())
print(count)