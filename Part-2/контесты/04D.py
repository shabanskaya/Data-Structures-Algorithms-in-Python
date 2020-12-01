x1, y1, x2, y2 = list(map(int, input().split()))
xa, ya = list(map(int, input().split()))
MAn = (x2-x1)*(ya - y1) - (xa - x1)*(y2 - y1)
modn = ((y1 - y2)**2 + (x1- x2)**2)**0.5
AOx = - MAn*(y2 - y1)/(modn**2)
AOy = MAn*(x2 - x1)/(modn**2)
z1 = xa - 2*AOx
z2 = ya - 2*AOy
print(z1, z2)
