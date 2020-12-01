a = int(input())
count_loc = 1
count_glob = 1
maxi = a

while a != 0:
    b = int(input())
    if b != 0:
        count_glob += 1
        if b == maxi:
            count_loc +=1
        if b > maxi:
            count_loc = 1
            maxi = b
    a = b

print(count_glob - count_loc)