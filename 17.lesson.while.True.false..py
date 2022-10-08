# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 15:38:59 2022

@author: qomon
"""

ask='Please write your age: \n'
while True:
    value=input(ask)
    if value=='exit' or value=='quit':
         break
    age=int(value)
     
    if age<7:
         price='2000'
    elif 7<=age<18:
        price='3000'
    elif 18<=age<65:
        price='10000'
    else:
        price="0"
    if price==0:
        print('its free')
    else:
        print(f'the ticket price is {price}')