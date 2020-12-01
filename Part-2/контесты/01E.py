n = int(input())
a = [0 for i in range(n)]
for i in range(n):
    a[i] = input().split()
for i in range(n):
    for j in range(n):
        print(a[j][i], end = " ")
    print()
    