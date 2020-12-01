def sorti(a):
    n = len(a)
    for i in range(1, n):
        for s in range(i-1, -1, -1):
            if a[s+1] < a[s]:
                a.insert(s, a.pop(s+1))
    return a

def sumc(x):
    i = 0
    while x//(10) != 0:
        i += x % 10
        x = x // 10
    i+=x
    return i

n = int(input())
a = []
s = []
for i in range(n):
    a.append(int(input()))
    s.append(sumc(a[i]))
    
for _ in range(n):
    for i in range(n-1):
        if s[i] > s[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            s[i], s[i+1] = s[i+1], s[i]
            
j = 0
while j < n-1:
    if s[j] == s[j+1]:
        k = j
        c = j+1
        while j != n-1 and s[j] == s[j+1]:
            c+=1
            j+=1
        a[k:c] = sorti(a[k:c])
    else:
        j+=1

for j in range(n):
    print(a[j])