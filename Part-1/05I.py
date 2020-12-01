n = int(input())
s = input()
a = s.split()
for i in range(n):
    a[i] = int(a[i])

s = [1]
for i in range(n):
    if a[i] == 1:
        c = 1
        b = 1
        if i == 0:
            b = -5
        if i > 0:
            for ii in range (i-1, -1, -1):
                if a[ii] != 2:
                    b+=1
                else:
                    break
            else:
                b = -3
        for ii in range (i+1, n):
            if a[ii] != 2:
                c+=1
            else:
                break
        else:
            c = -4
        if c > 0:
            if b > 0:
                s.append(min(b,c))
            else:
                s.append(c)
        else:
            s.append(b)
print(max(s))