# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 16:43:19 2022

@author: qomon
"""

import re
words = """ Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://jovian.ai/anvarnarz/38-python/v/4?utm_source=embed Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"""
template = ' https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*) '
web= re.findall(template, words)
print(web)
