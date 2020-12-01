a = list(map(int, input().split()))

n = len(a)

for x in range(n):
    for i in range(n-1):
        j = i+1
        while a[i]*a[j] < 0:
            j+=1
            if j == len(a):
                break
        if j < len(a):
            if (a[i]>0 and a[i]*a[j] > 0 and a[i]>a[j]):
                s = a[i]
                a[i] = a[j]
                a[j] = s
                print(*a)
            elif a[i]<0 and a[i]*a[j] > 0 and a[i]<a[j]:
                s = a[i]
                a[i] = a[j]
                a[j] = s
                print(*a)

