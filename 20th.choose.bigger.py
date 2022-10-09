# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 18:55:52 2022

@author: qomon
"""

def bigger(x,y,z):
    max=x
    if y>=max:
        max=y
    if z>=max:
        max=z
    return max
bigger(15,25,60)
