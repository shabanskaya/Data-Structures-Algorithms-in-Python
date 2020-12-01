def rec_sort(a, b = []):
    if len(a) <= 1:
        return 
    k = min(a)
    i = a.index(k)
    a[0], a[i] = a[i], a[0]
    b.append(a[0])
    
    c = b[0:len(b)-1] + a[:]
    if a[0] != a[i]:
        print(*c)
    rec_sort(a[1:])
    

a = list(map(int, input().split()))
rec_sort(a)