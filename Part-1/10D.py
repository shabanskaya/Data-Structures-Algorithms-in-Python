n = int(input())
y = [0]
for i in range(n):
    y.append(int(input()))
if n != 1:
    a = [0, 0, abs(y[2] - y[1])] + [0]*(n-2)
    
    for i in range(3, n+1):
        c1 = a[i-1] + abs(y[i-1] - y[i])
        c2 = a[i-2] + 3 * abs(y[i-2] - y[i])
        a[i] = min(c1, c2)
    
    print(a[n])
if n == 1:
    print(0)