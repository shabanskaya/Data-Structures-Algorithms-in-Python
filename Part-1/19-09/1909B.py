n = int(input())
s = 0
s += n % 10
s += (n // 10) % 10
s += n // 100
print (s)