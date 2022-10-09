# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 19:04:43 2022

@author: qomon
"""

def circle_info(radius,pi=3.1415):
    circle={'radius':radius,
            'diameter':2*radius,
            'perimeter':2*radius*pi,
            'surface':pi*radius**2}
    return circle
circle_info(55)