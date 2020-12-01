def simp(a):
    sq = int(a**0.5) + 1
    for i in range (2, sq):
        if a % i == 0:
            return False
    return True
c = 0
i = 2    
n = int(input())
while c != n:
    if simp(i):
        c+=1
    i+=1
print(i-1)