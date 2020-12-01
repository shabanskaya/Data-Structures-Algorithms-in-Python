n = int(input())
s = input()
a = s.split()
for i in range(1, n-1):
    if (int(a[i]) > int(a[i-1])) and (int(a[i]) > int(a[i+1])):
        print(i, end = ' ')
    elif (int(a[i]) < int(a[i-1])) and (int(a[i]) < int(a[i+1])):
        print(i, end = ' ')