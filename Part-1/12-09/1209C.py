#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 10:11:23 2019

@author: macbook
"""
def coco(q, w, e):
    cosin = (q**2 + w**2 - e**2) / (2 * q * w)
    return cosin

a = int(input())
b = int(input())
c = int(input())
if a == 0 or b == 0 or c == 0:
        print ("impossible")
else:

    u1 = coco(a, b, c)
    u2 = coco(a, c, b)
    u3 = coco(b, c, a)

    if (a+b<=c) or (a+c<=b) or (b+c<=a):
        print ("impossible")
    
    elif u1 == 0 or u2 == 0 or u3 == 0:
        print ("right")
        
    elif (u1<0 and u1>-1) or (u2<0 and u2>-1) or (u3<0 and u3>-1):
        print ("obtuse")
    
    else:
        print("acute")