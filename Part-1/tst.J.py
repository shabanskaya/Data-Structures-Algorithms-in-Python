n = int(input())
a = [0]
b = [1]
a[0] = input()
for i in range(n-1):
    s = input()
    for k in range(len(a)):
        if a[k] == s:
            b[k] += 1
            break
    else:
        a.append(s)
        b.append(1)
d = len(a)
for e in range(d):
    for ee in range(d):
        if b[ee] == max(b):
            print(a[ee], b[ee], sep = ' ')
            b[ee] = 0
            break