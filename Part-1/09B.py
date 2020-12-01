def rec(a, k, l, h):
    if l>h:
        return -1
    m = (l+h) // 2
    if a[m] == k:
        return m + 1
    elif a[m] < k:
        return rec(a, k, m+1, h)
    elif a[m] > k:
        return rec(a, k, l, m-1)

a = list(map(int, input().split()))
k = int(input())

l = 0
h = len(a)-1

print(rec(a, k, l, h))