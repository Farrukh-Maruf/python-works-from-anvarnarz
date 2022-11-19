# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 21:45:51 2022

@author: qomon
"""

def even_number(x):
    numbers=[]
    for i in x:              
        if i%2==0:
            numbers.append(i)
    return numbers