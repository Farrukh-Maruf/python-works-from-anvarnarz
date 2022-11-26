# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 14:57:16 2022

@author: qomon
"""

import datetime as dt
import math
b_day= dt.date(2001,4,20)
t_year=dt.date(2022,4,20)
today=dt.date.today()
change= (t_year-b_day).days
year=change/365
m_days= (today-t_year).days
month=m_days/30
days= (today-dt.date(2022,11,20)).days



print(f'there are {math.floor(year)} years, {math.floor(month)} months, {days} days passed since my birthday.')