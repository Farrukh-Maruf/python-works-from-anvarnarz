# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 16:20:16 2022

@author: qomon
"""

orders=[]
while True:
    food=input("please, order food: \n")
    orders.append(food.title())
    answer=input("do u want to add more? yes/no")
    if answer!='yes':
        break
    else:
        continue
print('your order list' orders)