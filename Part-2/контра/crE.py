n, t = list(map(int, input().split()))
a = []
for i in range(n):
    x, y = input().split()
    y = int(y)
    a.append([x, y])

m = int(input())

i = 0
s = 0
while len(a)>1 and s+i < m:
    h = a[i%len(a)][1]
        
    if h == 0:
        if t == 0:
            t = 1 #chto skasal
            a[i%len(a)][1] = 1
            i+=1
        elif t == 1:
            t = 0
            i+=1
                
    elif h == 1:
        if t == 0:
            x = a.pop(i%len(a))
            s+=1
        if t == 1:
            i+=1

for i in range(len(a)):
    print(*a[i])
    
        