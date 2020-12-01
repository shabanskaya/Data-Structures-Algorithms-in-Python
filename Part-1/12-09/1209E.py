#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 10:47:13 2019

@author: macbook
"""

a = int(input())
s = input()

if s == "monkey":
    b = a//90
elif s == "elephant":
    b = a//300
elif s == "parrot":
    b = a//10

if b == 0:
    print(1)
else:
    print (b)