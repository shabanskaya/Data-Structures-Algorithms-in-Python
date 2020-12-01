n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
kaka = input()
c = list(map(int, input().split()))
w = 0
for i in range(n):
    for k in range(i, n):
        if a[i][k] == 1 and c[i]!=c[k]:
            w+=1
print(w)