# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 10:57:28 2022

@author: qomon
"""

davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }
davlat=input('choose any country: ').lower()
if davlat in davlatlar:
    info=davlatlar[davlat]
    print(f"{davlat.capitalize()} capital is {info['poytaxt'].title()}"
          f'\n The area of {davlat.capitalize()} is {info["maydon"]}'
          f'\n The population is {info["aholi"]}'
          f'\n the money is {info["pul birligi"]}'
          )
else:
    print(f'we have no info about {davlat.capitalize()}')