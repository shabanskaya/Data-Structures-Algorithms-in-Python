n = int(input())
a = [0 for c in range(n)]
for i in range(n):
    a[i] = int(input())
for i in range(n):
    print(a[n-i-1])