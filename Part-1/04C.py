def cub(ii):
    if ii == 0 or ii == 1:
        return True
    else:
        v = 2
        while v < round(ii**(0.333333333))+2:
            if ii == v**3:
                return True
            else:
                v+=1
        return False

n = int(input())
c = 0
i = 0
while (n - i**3) >= i**3:
    ii = (n - i**3)
    if cub(ii):
        print (i, round(ii**(1/3)))
        c=1
        break
    i+=1
if c == 0:
    print("impossible")
