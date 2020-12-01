def kon(x, y, a, b):
    def za_1(x,y,a,b):
        if (abs(x-a) == 2 and abs(y-b) == 1) or (abs(x-a) == 1 and abs(y-b) == 2):
            return 1
        return 0
    if x == a and y == b:
        return 0
    if za_1(x, y, a, b):
        return 1
    elif za_1(x-2, y-1, a, b) == 1 or za_1(x-2, y+1, a, b) == 1 or za_1(x+2, y-1, a, b) == 1 or za_1(x+2, y+1, a, b) == 1 or za_1(x-1, y-2, a, b) == 1 or za_1(x-1, y+2, a, b) == 1 or za_1(x+1, y-2, a, b) == 1 or za_1(x+1, y+2, a, b) == 1:
        return 2
    else:
        return -1

x = int(input())
y = int(input())
a = int(input())
b = int(input())
print(kon(x, y, a, b))