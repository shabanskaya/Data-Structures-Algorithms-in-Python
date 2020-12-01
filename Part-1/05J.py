def final(x, y, n, m):
    a = 0
    if x +1 == n or y + 1 == m or x - 1 < 0 or y - 1 < 0:
        a += 1
    return a


if __name__ == '__main__':
    n, m = input().split()
    n, m = int(n), int(m)
    a = [[0]*m for i in range(n)]
    x, y = 0, 0
    for i in range(n):
        j = 0
        s = input()
        for w in s:
            if w == '#':
                a[i][j] = -1
            if w == ' ':
                a[i][j] = 0
            if w == '@':
                a[i][j] = 1
                x, y = i, j
            j += 1
    while True:
        c = 0
        z = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] == 1:
                    x, y = i, j
                    if final(x, y, n, m) == 1:
                        print('YES')
                        z=6
                        break
                    if a[i-1][j] != -1:
                        a[i - 1][j] += 1
                    if a[i+1][j] != -1:
                        a[i+1][j] += 1
                    if a[i][j-1] != -1:
                        a[i][j-1] += 1
                    if a[i][j+1] != -1:
                        a[i][j+1] += 1
                    if a[i][j] != -1:
                        a[i][j] += 1
                else:
                    c += 1
            if z == 6:
                    break
        if z == 6:
                break
        if c == m*n:
            print('NO')
            break