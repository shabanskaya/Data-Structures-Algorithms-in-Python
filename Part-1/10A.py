F = [-1]*105

def fib(n):
    if n <= 1:
        return 1
    if F[n] == -1:
        F[n] = fib(n-1) + fib(n-2)
    return F[n]

n = int(input())
print(fib(n))