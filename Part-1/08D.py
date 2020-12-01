def hoar_sort(A, depth=1, part='left'):
    print('depth:', depth, 'part:', part, 'array before:', A)
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
    
    print('depth:', depth, 'part:', part, 'array after:', A)
