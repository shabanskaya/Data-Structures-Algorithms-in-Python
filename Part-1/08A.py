def merge (A, B):
    aa = len(A)
    bb =len(B)
    C = [0 for i in range(aa+ bb)]
    a = 0
    b = 0
    c = 0
    while a < aa and b < bb:
        if A[a] <= B[b]:
            C[c] = A[a]
            a+=1
            c+=1
        else:
            C[c] = B[b]
            b+=1
            c+=1
    if a == aa:
        while c < len(C):
            C[c] = B[b]
            b+=1
            c+=1
    else:
        while c < len(C):
            C[c] = A[a]
            a+=1
            c+=1
    return C
