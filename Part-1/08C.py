def split_barrier(A, barrier):
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
            
    k = 0
    for x in L+M+R:
        A[k] = x
        k+=1

