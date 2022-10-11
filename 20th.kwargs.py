# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 10:57:38 2022

@author: qomon
"""

def students_info(name,surname,**kwargs):
    kwargs['name']=name
    kwargs['surname']=surname
    return kwargs
student=students_info("farrukh",'marufjonov',tyil=2001,yashash='incheon')