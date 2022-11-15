# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 15:15:38 2022

@author: qomon
"""
import json
talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
name= json.loads(talaba_json)
print(name['ism'], name['familiya'])