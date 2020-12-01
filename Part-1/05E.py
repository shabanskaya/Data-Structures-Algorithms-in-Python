n = int(input())
s = input()
a = s.split()
for i in range(n):
    a[i] = int(a[i])
for i in range(n):
    for ii in range (i, n):
        if a[ii] != a[n-ii+i-1]:
            break
    else:
        print(i)
        for iii in range(i):
            print(a[i-iii-1], end = ' ')
        break