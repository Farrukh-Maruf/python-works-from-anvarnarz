# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 14:44:50 2022

@author: qomon
"""

import datetime as dt
today=dt.date.today()
eid_fitr= dt.date(2023,4,21)
adha= dt.date(2023,6,28)
days_left= eid_fitr- today
day_left= adha-today
print(f'There are {days_left.days} days left for EID UL FITR.\n'
      f'There are {day_left.days} days left for EID UL ADHA')
