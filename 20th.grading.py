# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 10:13:57 2022

@author: qomon
"""

names=['ali','vali','nal','kami']
def grading(students):
    grades={}
    for name in students:
        grade=input(f"What is grade for {name.title()}?  ")
        grades[name]=grade
    return grades
grades=grading(names)
print(grades)