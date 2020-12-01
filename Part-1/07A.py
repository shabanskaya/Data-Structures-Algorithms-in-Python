def matryoshka(n):
    def pech(a, i):
        if i == len(a):
            return 0
        print(a[i])
        return pech(a, i+1)
    
    a = list(range(n, 1, -1))
    a = list(map(lambda x:'verh matryoshki ' + str(x), a))
    pech(a, 0)
    
    print ('matryoshechka')
    
    b = list(range(2, n+1))
    b = list(map(lambda x:'niz matryoshki ' + str(x), b))
    pech(b, 0)
