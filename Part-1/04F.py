n = int(input())
f = 1
for i in range(1, n+1):
    f *= i
c = 0
f = str(f)
for i in range (len(f)):
    if f[i] == "0":
        c+=1
print(f, c)