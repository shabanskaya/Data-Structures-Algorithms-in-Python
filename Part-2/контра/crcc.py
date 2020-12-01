a = input().split()
i = 2
s = 0
d = {}
if len(a) == 2:
    pass
else:
    while a[i] != '=':
        if a[i] == '+':
            if i>=2:
                if a[i-1] isdigit():
                    a[i-1] = int(a[i-1])
                else:
                    while a[i-1] is not in d:
                        x = input().split()
                        d.append()
                a.pop(i)
                i-=2
                a[i]+=a.pop(i+1)
            else:
                s = 1
                break
        if a[i] == '*':
            if i>=2:
                a.pop(i)
                i-=2
                a[i]*=a.pop(i+1)
            else:
                s = 1
                break
        if a[i] == '/':
            if i>=2:
                a.pop(i)
                i-=2
                a[i] //= a.pop(i+1)
            else:
                s = 1
                break
        
        