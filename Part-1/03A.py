def nod(a, b):
    while b!=0:
        a, b = b, a%b
    return a

a = int(input())
b = int(input())
print(nod(a, b))