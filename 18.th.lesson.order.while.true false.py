# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 19:45:51 2022

@author: qomon
"""

orders=[]
products={}
while True:
    food=input("please, order food: \n")
    orders.append(food.title())
    answer=input("do u want to add more? yes/no")
    if answer!='yes':
       break
   

while True:
      product=input("Please,add product- ")
      price=input(f'please,refer to the price of {product} ')
      products[product]=price
      answer=input('Do you want to add more? yes/no')
      if answer!='yes':
          break
while orders:
    food=orders.pop()
    if food in products:
        foodprice=products[food]
        print(f'{food}price is {foodprice}.')
    else:
        print(f'we do not have {food}')
    
