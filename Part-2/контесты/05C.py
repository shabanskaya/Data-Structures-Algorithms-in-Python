def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
a = []
x = input()
while x != "=":
    if isfloat(x):
        x = float(x)
    a.append(x)
    x = input()

i = 0
while len(a) > 1:
    if isfloat(a[i]):
        i+=1
    
    if a[i] == "+":
        a[i] = 0
        x1 = a.pop(i-1)
        x2 = a.pop(i-2)
        a[i-2] = x1+x2
        i = i-1
        
    elif a[i] == "-":
        a[i] = 0
        x1 = a.pop(i-1)
        x2 = a.pop(i-2)
        a[i-2] = x2-x1
        i = i-1
        
    elif a[i] == "*":
        a[i] = 0
        x1 = a.pop(i-1)
        x2 = a.pop(i-2)
        a[i-2] = x1*x2
        i = i-1
print(int(a[0]))