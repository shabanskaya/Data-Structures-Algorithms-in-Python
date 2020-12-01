a = list(input())
for i in range(len(a)):
    a[i] = int(a[i])
a.sort()
j = 0
while a[j] == 0:
    j+=1
s = str(a[j]) + '0'*j
for i in range(j+1, len(a)):
    s+=str(a[i])
print(int(s))