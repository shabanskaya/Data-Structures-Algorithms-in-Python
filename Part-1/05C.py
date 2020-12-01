n = int(input())
a = [0 for c in range(n)]
for i in range(n):
    a[i] = int(input())
x = int(input())
c = 0
for i in range(n):
    if a[i] % x == 0:
        c = 1
        print(i, end = ' ')
if c == 0:
    print(-1)