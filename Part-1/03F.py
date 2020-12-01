a = input()
maxi = 0
c = '0'
i = 0
while i<(len(a)):
    if (a[i].isdigit()):
        c += a[i]
        maxi = max(maxi, int(c))
        i+=1
    else:
        maxi = max(maxi, int(c))
        c = '0'
        i+=1
print(maxi)