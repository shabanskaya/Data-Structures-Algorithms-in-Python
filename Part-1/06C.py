a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])

n = len(a)
s = 0
while s != n-1:
    if a[s] > a[s+1]:
        a.insert(s, a.pop(s+1))
        s = 0
        print(*a)
    else:
        s+=1

    