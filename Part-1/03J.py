a = int(input())
s = ''
i = 0
while a // 60 >= 1:
    number = a // (60**i) % 60
    n1 = number//10
    n2 = number%10
    s = ('<' * n1) + ("v" * n2) + "." + s
    a = a // 60
number = a // (60**i) % 60
n1 = number//10
n2 = number%10
s = ('<' * n1) + ("v" * n2) + "." + s
print(s[:len(s)-1])