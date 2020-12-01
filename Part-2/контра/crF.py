a = input().split()
d = []
c = []
err = 0

if len(a) == 2:
    pass
else:
    for i in range(len(a)):
        if a[i].isdigit():
            d.append(int(a[i]))
            
        elif (a[i] == '+' or a[i] == '*' or a[i] == '/') and len(d)<2:
            err = 1
            break
        elif a[i] == '+' and len(d) >= 2:
            d[len(d)-2] += d.pop(len(d) - 1)
        elif a[i] == '-' and len(d) >= 2:
            d[len(d)-2] -= d.pop(len(d) - 1)
        elif a[i] == '*' and len(d) >= 2:
            d[len(d)-2] *= d.pop(len(d) - 1)
        elif a[i] == '/' and len(d) >= 2:
            d[len(d)-2] //= d.pop(len(d) - 1)
        elif a[i] == '=':
            break
        
        else:
            j = 0
            if len(c) == 0:
                c.append(input().split())
                if c[j][2] == '=':
                    c[j][1] = int(c[j][1])
                else:
                    err = 1
                    break
            while c[j][0] != a[i]:
                c.append(input().split())
                if c[j][2] == '=':
                    c[j][1] = int(c[j][1])
                else:
                    err = 1
                    break
                j+=1
            d.append(int(c[j][1]))
            

if err == 0 and len(d) == 1:
    print(*d)
else:
    print('incorrect')
            
        

            
            
        
            