s = input()
n = len(s)
a = [0] * n
a[0] = 1
for i in range(1, n):
    for k in range(i+1):
        if k<i:
            if s[0:k+1] == s[i:i-k-1:-1]:
                a[i] = k+1
            else:
                break
        if k == i:
            if s[0:k+1] == s[i::-1]:
                a[i] = k+1
    
print(*a)