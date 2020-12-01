def minor(a, i, j):
    m = [[] for _ in range(len(a))]
    for s in range(len(a)):
        for ss in range(len(a)):
            m[s].append(a[s][ss])
    x = m.pop(i)    
    for s in range(len(m)):
        x = m[s].pop(j)
    return m   
    
def det(a, n):
    if n == 1:
        return a[0][0]
    znak = 1
    determinant = 0
    for j in range(n):
        determinant += a[j][0] * znak * det(minor(a, j, 0), n-1) 
        znak *= -1
    return determinant                           

n = int(input())
a = []      
for i in range(n):
    a.append(list(map(int, input().split())))
                   

print(det(a, n))
            
        