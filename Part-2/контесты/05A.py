a = input().split()
for i in range(len(a)):
    a[i] = list(a[i])
    a[i][1] = int(a[i][1])
i = 0
c = 0
while i < len(a)-1:
    if a[i][0] == a[i+1][0] and abs(a[i][1]-a[i+1][1]) <= 2:
        x = a.pop(i)
        x = a.pop(i)
        c+=1
        if i>1:
            if a[i-1][0] == a[0][0]:
                x = a.pop(i-1)
                x = a.pop(0)
                i = i-2
                c+=1
    else:
        i+=1
print(2*c)
            