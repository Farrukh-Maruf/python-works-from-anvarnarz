# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 10:20:54 2022

@author: qomon
"""

#movies=print('please, write 3 movies you like most:\n')
#movie=[]
#for n in range(3):
  #  movie.append(input(f'{n+1} movie').title())
#print(f'Anvar quyidagi kinolarni yaxshi koradi:{movie}')
 

movies={'mother':['love','thunder'],
        'father':['thor','wonder women'],
        'brother':['spiderman','no way home'] }
for names,keys in movies.items():
    print(f'{names.title()} likes:')
    for key in keys:
        print(key.title())