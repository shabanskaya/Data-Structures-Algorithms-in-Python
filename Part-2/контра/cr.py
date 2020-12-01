a = list(input())
b = []
z = 0
for i in range(len(a)):
    if a[i] == '(' or a[i] == '[' or a[i] == '{':
        b.append(a[i])
    
    elif a[i] == ')':
        if len(b) == 0:
            z = 1
            break
        elif (b[len(b)-1]) != '(':
            z = 1
            break
        else:
            x = b.pop()

    
    elif a[i] == ']':
        if len(b) == 0:
            z = 1
            break
        elif (b[len(b)-1]) != '[':
            z = 1
            break
        else:
            x = b.pop()
    
    elif a[i] == '}':
        if len(b) == 0:
            z = 1
            break
        elif (b[len(b)-1]) != '{':
            z = 1
            break
        else:
            x = b.pop()

if z == 0 and len(b) == 0:
    print('YES')
else:
    print("NO")