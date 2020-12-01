s = 1
b = int(input())
min = b
while b != 0:
    b = int(input())
    if b < min and b!=0:
        min = b
        s = 1
    elif b == min:
        s+=1
print(s)
