# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 13:08:47 2022

@author: qomon
"""

def consumer_info(name,surname,birth,place,email='',number=None):
    consumer={'name':name,
              'surname':surname,
              'birth':birth,
              'place':place,
              'email':email,
              'number':number}
    return consumer
print('Please, give information about the consumer:')
consumers=[]
while True:
    name=input('Please write consumer name:')
    surname=input('please write the surname: ')
    birth=int(input('please write year of birth:' ))
    place=input("please write your birth place:")
    email=input('please write email address: ')
    number=input("please write the phone number: ")
    consumers.append(consumer_info(name,surname,birth,place,email,number))
    answer=input('Do you want to keep on? yes/no ')
    if answer!='yes':
        break
print('Consumers:') 
for consumer in consumers:
    print(f'{consumer["name"].title()} {consumer["surname"].title()}.'
          f"{consumer['birth']} born in {consumer['place']}."
          f"he/she is {2020-consumer['birth']}, phone number is {consumer['number']}.")
          