def hoar_sort(A, depth=1, part='left'):
    if len(A) <= 1:
        return
    barrier = A[0]
    R = []
    M = []
    L = []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L, depth = depth+1, part='left')
    hoar_sort(R, depth = depth+1, part='right')
    
    k = 0
    for x in L+M+R:
        A[k] = x
        k+=1
    return A

n = int(input())
a = list(map(int, input().split()))
hoar_sort(a)

s = 0
for i in range(n//2+1):
    s+=a[i]//2+1
print(s)