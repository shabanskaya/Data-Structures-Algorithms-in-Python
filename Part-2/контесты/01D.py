n = int(input())
s = list(map(int, input().split()))

c = []

for i in range(1, n-1):
    if (s[i] > s[i-1] and s[i] > s[i+1]) or (s[i] < s[i-1] and s[i] < s[i+1]):
        c.append(i)
print(*c)