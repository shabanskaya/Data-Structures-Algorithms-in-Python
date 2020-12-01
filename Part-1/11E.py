d = input()
c = input()
s = d + '#' + c
n = len(s) 
z = [0] * n
left = right = 0
for i in range(1, n):
    if i <= right:
        x = min(z[i-left], right - i + 1)
    else:
        x = 0
    while i+x < n and s[x] == s[i+x]:
        x+=1
    z[i] = x
    if i + x - 1 > right:
        left, right = i, i+x-1

x = 1

for i in range(len(d), n):
    if z[i] == len(d):
        print(i-len(d)-1, end = ' ')
        x=4
if x == 1:
    print(-1)