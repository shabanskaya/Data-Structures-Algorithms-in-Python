
summ, numm = input().split()
summ = int(summ)
numm = int(numm)

c = ""
if numm*9 < summ or numm > summ:
    print ("impossible")

else:
    for i in range(numm, 0, -1):
        if (summ - i + 1) // 9 == 0:
            a = (summ - i + 1) % 9
        else:
            a = 9
        c = str(a) + c
        summ -= a
    print (c)

    