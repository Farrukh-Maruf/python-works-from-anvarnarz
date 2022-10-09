# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:57:14 2022

@author: qomon
"""
qoldiqsz=[]
def qoldiq(x):
    for n in range(2,11):
        if not x%n:
            qoldiqsz.append(n)
            
qoldiq(20)
print(qoldiqsz)            