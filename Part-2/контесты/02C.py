def search(table, key):
    s = key
    h = 0
    for c in s:
        h = (h*91 + ord(c)) % 100
    p = h%10
    for e in table[p]:
        if e[1] == s:
            return e[2]
    return 'KeyError'