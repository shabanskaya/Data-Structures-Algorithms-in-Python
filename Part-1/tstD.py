a = []
a.append(input())
while a[len(a)-1] != "#":
    a.append(input())
c = a.pop()

summ = 0
for i in range(len(a)):
    a[i] = int(a[i])
    summ += a[i]
av = round(summ/len(a), 3)

s = 0
for i in range(0, len(a), 3):
    s += (a[i] + a[i+1] + a[i+2]) % a[i+2]

print(av, max(a), min(a), s)