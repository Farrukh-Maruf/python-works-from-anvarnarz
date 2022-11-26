# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 14:23:52 2022

@author: qomon
"""

import datetime as dt
today=dt.datetime.now()
tdate=today.date()
changes=0
for x in range(10):
    f_days=tdate+ dt.timedelta(days=changes)
    changes +=14
    print(f_days)
    
