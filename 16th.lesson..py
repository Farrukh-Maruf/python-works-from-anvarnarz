# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 15:52:46 2022

@author: qomon
"""
buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
           'tyil':810,
           'vyil':870,
           'tjoy':'Buxoro'
           }

qodiriy = {'ism':'Abdulla Qodiriy',
           'tyil':1894,
           'vyil':1938,
           'tjoy':'Toshkent'
           }

vohidov = {'ism':'Erkin Vohidov',
           'tyil':1936,
           'vyil':2016,
           'tjoy':"Farg'ona"
           }

navoiy = {'ism':'Alisher Navoiy',
           'tyil':1441,
           'vyil':1501,
           'tjoy':"Xirot"
           }
names=[buxoriy,qodiriy,vohidov,navoiy]
for k in names:
    name=k['ism']
    birth=k['tyil']
    death=k['vyil']
    place=k['tjoy']
    print(f'{name} {birth} da tugilgan.'
          f'{death-birth} yil umr korgan.'
          f'{place} da tugilgan.')