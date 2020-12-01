n = int(input())
c = [0] + list(map(int, input().split()))
p = [0] + list(map(int, input().split()))
a = [0, 1] + [0]*(n-1)

x = c[1]
for i in range(1, n-1):
    if c[i] == c[i+1] or p[i] == c[i+1]:
        a[i+1]+=a[i]
    if c[i] == c[i+2] or p[i] == c[i+2]:
        a[i+2]+=a[i]

if c[n-1] == c[n] or p[n-1] == c[n]:
    a[n]+=a[n-1]
print(a[n]%947)
    