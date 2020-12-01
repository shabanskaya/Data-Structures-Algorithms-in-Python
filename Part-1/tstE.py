p = int(input())
if p <= 2:
    print("YES")
elif (2**(p-1))%p == 1:
    print("YES")
else:
    print("NO")