# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 16:23:18 2022

@author: qomon
"""
import re
template= '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
msg='Please, inter a phone number:\n'
while True:
    phonenumber=input(msg)
    if re.match(template,phonenumber):
        print('accepted, thank you')
        break
    else:
        print('try again')