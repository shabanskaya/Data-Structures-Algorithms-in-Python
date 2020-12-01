n = int(input())
m = int(input())
k = int(input())
a = [[] for c in range(n)]
for i in range(n):
    for ii in range(m):
        a[i].append(0)

for i in range(k):
    y = int(input())
    x = int(input())
    a[y-1][x-1] = -1
    
for i in range(n):
    for ii in range(m):
        if a[i][ii] != -1:
            if (ii-1) >= 0 and i-1 >= 0:
                if a[i-1][ii-1] == -1:
                    a[i][ii] += 1
            if (ii+1) < m and i-1 >= 0:
                if a[i-1][ii+1] == -1:
                    a[i][ii] += 1
            if (ii+1) < m and i+1 < n:
                if a[i+1][ii+1] == -1:
                    a[i][ii] += 1
            if (ii-1) >= 0 and i+1 < n:
                if a[i+1][ii-1] == -1:
                    a[i][ii] += 1
            
            if (ii+1) < m:
                if a[i][ii+1] == -1:
                    a[i][ii] += 1
            if (ii-1) >= 0:
                if a[i][ii-1] == -1:
                    a[i][ii] += 1
            if i + 1 < n:
                if a[i+1][ii] == -1:
                    a[i][ii] +=1
            if i-1 >= 0:
                if a[i-1][ii] == -1:
                    a[i][ii] += 1

for i in range(n):
    print(*a[i])