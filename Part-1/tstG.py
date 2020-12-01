a = input()
a = list(a)
n = 0
i = len(a) - 1
x = 0
while i >= 0:
    if a[i] == 'v':
        n+=60**x
        i -= 1
    if a[i] == '<':
        n+=10*(60**x)
        i -= 1
    if a[i]== '.':
        x+=1
        i-=1
print(n)