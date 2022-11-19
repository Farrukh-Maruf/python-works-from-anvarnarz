# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 15:32:28 2022

@author: qomon
"""

def get_number(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        big_number=z
    return big_number
