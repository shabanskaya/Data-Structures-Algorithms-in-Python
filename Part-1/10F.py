n = int(input())
if n%2 == 0:
    n = n//2
    a = [1, 3] + [0]*(n)
    for i in range(2, n+1):
        a[i] = 4*a[i-1] - a[i-2]
    print(a[n])
else:
    print(0)