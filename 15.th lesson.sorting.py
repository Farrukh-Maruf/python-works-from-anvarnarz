# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 14:08:59 2022

@author: qomon
"""

davlatlar = {
    "uzbekistan":'tashkent',
    'USA':'Washington d.c.',
    'RUSSIAN':'moscow',
    'tajikistan':'dushanbe',
    "kyrgyzstan":'bishkek',
    'qazaqstan':'nursultan',
    'malaysian':'kuala-lumpur',
    'singapore':'singapore',
    'italy':'rome'}
davlat=input(" please choose any country: ")
capital=davlatlar.get(davlat.lower())
if capital==None:
    print("we have no knowledge")
    
else:
    print(f'{davlat.title()} capital is {capital.title()}')