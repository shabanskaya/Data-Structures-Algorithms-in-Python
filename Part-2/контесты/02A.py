def code(c):
    return ord(c)

def poly_hash (s, b, M):
    h=0
    for c in s:
        h = (h*b + code(c)) % M
    return h

b, M = list(map(int, input().split()))
s = input()

print(poly_hash(s, b, M))