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

def deal(a):
    c = [a[0]]
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            c.append(a[i])
    return c

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
hoar_sort(a)
hoar_sort(b)

v = deal(a)
w = deal(b)

if len(v) == len(w):
    s = 0
    for i in range(len(v)):
        if v[i] == w[i]:
            s+=1
        else:
            break
    if s == len(w):
        print('Yes')
    else:
        print('No')
else:
    print('No')
        
