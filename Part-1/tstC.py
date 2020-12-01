n = int(input())
s = 1
for i in range(n):
    for k in range(i+1):
        print(s, end = " ")
        s+=1
    print()
    