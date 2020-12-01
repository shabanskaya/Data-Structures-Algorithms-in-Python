
def remove(table, key):
    s = key
    h = 0
    for c in s:
        h = (h*91 + ord(c)) % 100
    p = h%10
    for e in range(len(table[p])):
        if table[p][e][1] == s:
            x = table[p][e][2]
            del table[p][e]
            return x
    return 'KeyError'
