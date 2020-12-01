#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 09:50:01 2019

@author: macbook
"""
print ('Знаю кучу четных чисел: ', end ='')
for i in range (15):
    if i % 2 == 0:
        print (i, end =', а ещё ')
print ("... ну ладно хватит")