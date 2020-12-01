n = int(input())
k = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])

l = 0
h = n-1
ind = 0

while l<=h:
    m = (l+h)//2
    if a[m] < k:
        l = m + 1
    elif a[m]>k:
        h = m - 1
    else:
        ind = m+1
        break
if ind == 0:
    print(-1)
else:
    print(ind)
        