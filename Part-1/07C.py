def f(n, k):
    if n == 1:
        return k
    return f(n-1, k) + 2*k + n-1 + n-2

k = int(input())
n = int(input())

print(f(n, k))