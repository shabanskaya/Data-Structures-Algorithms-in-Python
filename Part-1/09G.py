n = int(input())
a = []
b =[]
for i in range(n):
    k = int(input())
    for h in range(k):
        x, y = input().split()
        x = float(x)
        a.append(x)
        b.append(y)

n = len(a)

for _ in range(n):
    for i in range(n-1):
        if a[i] < a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            b[i], b[i+1] = b[i+1], b[i]
        if a[i] == a[i+1]:
            if b[i] < b[i+1]:
                b[i], b[i+1] = b[i+1], b[i]                
print(n)
for i in range(n):
    print(round(a[i], 2), b[i])
    
