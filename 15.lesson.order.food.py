# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 14:27:09 2022

@author: qomon
"""
menu={'steak':'3000',
      'pizza':'2000',
      'burger':'2500',
      'hot-dog':'1500',
      'fries':"1000"     
      }
print("Order 3 types of food")
orders=[]
for n in range(3):
    orders.append(input(f'{n+1}-order:').lower())
    
for order in orders:
    if order in menu:
        print(f'{order.title()} costs {menu[order]}.')
    else:
        print(f"Ups,sorry, we have no {order}.")