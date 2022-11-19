# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 15:40:50 2022

@author: qomon
"""


import unittest
from big_number import get_number

class NumberTest(unittest.TestCase):
    def test_big_number(self):
        formatted_number=get_number(15,15.01,16)
        self.assertEqual(formatted_number,16)
        
unittest.main()