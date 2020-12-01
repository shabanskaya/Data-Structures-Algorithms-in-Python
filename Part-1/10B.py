n = int(input())
s = [0] + list(map(int, input().split()))
a = [0, 1] + [0]*(n-1)

if 1+s[1]<=n and s[1]!=1:
    a[1+s[1]]+=1

for i in range(2, n+1):
    a[i] += a[i-1]
    if i+s[i]<=n and s[i]!=1:
        a[i+s[i]]+=a[i]
    #for z in range(i-1):
     #   if s[z] == i-z:
      #      a[i]+=a[z]
        


print(a[n]%937)