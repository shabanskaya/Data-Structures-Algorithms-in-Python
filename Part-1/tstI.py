n = int(input())
a = [input().split() for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = int(a[i][j])

s = []
m = 0
d1 = 0
d2 = 0
for i in range(n):
    for j in range(n):
        m += a[i][j]
    s.append(m)
    m = 0
    
    for j in range(n):
        m += a[j][i]
    s.append(m)
    m = 0
    
    d1+=a[i][i]
    d2+=a[i][n-i-1]
s.append(d1)
s.append(d2)

i = 0
while s[i] == s[i+1]:
    i += 1
    if i == len(s)-1:
        break
if i == len(s) - 1:
    print("YES")
else:
    print("NO")