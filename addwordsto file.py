# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 22:59:44 2022

@author: qomon
"""

import pickle
word1="i love you so much my mummy"

with open('words for mummy.dat','wb') as file:
    pickle.dump(word1,file)
    
    
with open('words for mummy.dat','rb') as file:
    word=pickle.load(file)
print(word)

add=True
while add:
    words=input('add your words for your mummy(<stop> for stopping): ')
    if words== 'stop': break
    with open('words for mummy.dat','a') as file:
        file.write(words+ '\n')
        
with open('words for mummy.dat','rb') as file:
    word=pickle.load(file)
print(word)