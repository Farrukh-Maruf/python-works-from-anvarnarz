# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 18:49:26 2022

@author: qomon
"""
def words(x=[]):
    words_with_capital=[]
    for m in x:
        words_with_capital.append(m.title())
    return words_with_capital