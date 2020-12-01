def merge_sort(A, depth=1, part='left'):
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
    
    print('depth:', depth, '|', 'part:', part, '|', 'array:', A)
    
    if len(A) == 1 or len(A) == 0:
        return 
    middle = len(A)//2
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L, depth=depth+1, part='left')
    
    merge_sort(R, depth=depth+1, part='right')
    C = merge(L, R)

    for i in range(len(C)):
        A[i] = C[i]

    print('depth:', depth, '|', 'part:', part, '|', 'after merge:', A) 
