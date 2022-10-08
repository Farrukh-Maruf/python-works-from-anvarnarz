# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 16:07:03 2022

@author: qomon
"""

print("Kiritilgan sonning ildizini qaytaruvchi dastur.\n")
savol = "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)    
    if qiymat=="exit": 
           break
    elif float(qiymat)<0:
           continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")