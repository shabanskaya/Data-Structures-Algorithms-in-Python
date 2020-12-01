n = int(input())
a = list(map(int, input().split()))

for i in range(len(a)):
    a[i] = int(a[i])

n = len(a)
for _ in range(n):
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]

sh = 0
cr = 0
for i in range(n//2):
    cr+=a[i]
for i in range(n//2, n):
    sh+=a[i]
print(sh-cr)