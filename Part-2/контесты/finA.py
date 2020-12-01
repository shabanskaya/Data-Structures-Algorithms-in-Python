a = list(map(int, input().split()))
n = len(a)
s = []
for i in range(n):
    if a[i]>0:
        s.append(a[i])
    elif a[i] < 0 and len(s)!=0:
        if a[i]*(-1)<s[-1]:
            s[-1] += a[i]
        else:
            x = s.pop()
if len(s) == 0:
    print(0, -1)
else:
    print(len(s), s[-1])