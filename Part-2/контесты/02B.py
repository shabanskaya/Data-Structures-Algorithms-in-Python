b = 91
M = 100
P = 10 #table size

def code(c):
    return ord(c)

def poly_hash (s):
    h=0
    for c in s:
        h = (h*b + code(c)) % M
    return h

def get_pos(h):
    return h%P 

def add(table, key, value):
    h = poly_hash(key)
    p = get_pos(h)
    for e in table[p]:
        if e[1] == key:
            e[2] = value
            return
    table[p].append([h, key, value])

table = [[] for _ in range(P)]
x = int(input())

for i in range(x):
    key, value = input().split() 
    add(table, key, value)
       
for i in range(len(table)):
    if len(table[i]) != 0:
        print(i)
        for y in range(len(table[i])):
            print(*table[i][y])
