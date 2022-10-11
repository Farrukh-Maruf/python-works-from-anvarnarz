# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 10:02:28 2022

@author: qomon
"""

def fibonacci(n):
    numbers=[]
    for x in range(n):
        if x==0 or x==1:
            numbers.append(1)
        else:
            numbers.append(numbers[x-1]+numbers[x-2])
    return numbers
fibonacci(15)
