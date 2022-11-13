# -*- coding: utf-8 -*-
# """
# Created on Sun Nov  6 14:41:52 2022

# @author: qomon
# filename='pi_txt.txt'

# with open('pi_txt.txt') as file:
#     pi=file.read()
# birthday='20042001'
# if birthday in pi:
#     print('yes there is ')
# else:
#     print('there is no')


import pickle
# info="i love you mommy"
# info1={'my mother name:':'Motabar','her age':'45'}
# with open('royhat.dat','wb') as file:
#     pickle.dump(info1,file)
#     pickle.dump(info,file)
with open('royhat.dat','rb') as file:
    infos=pickle.load(file)
    infos2=pickle.load(file)
print(infos2)
print(infos)