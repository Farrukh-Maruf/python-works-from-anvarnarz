# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 15:51:46 2022

@author: qomon
"""

def fibonacci(x):
    numbers=[]
    for n in range(x+1):
        if n==0 or n==1:
            numbers.append(n)
        else:
            numbers.append(numbers[n-1]+numbers[n-2])            
    if x in numbers:
        return True
    else: 
        return False
  