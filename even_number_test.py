# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 22:35:15 2022

@author: qomon
"""

import unittest
from even_number import even_number

class numberTest(unittest.TestCase):
    def test_even_number(self):
        x=[45, 28, 3286, 236, 3564, 35, 4786]
        even_numbers= even_number(x)
        numbers=[28,3286,236,3564,4786]
        self.assertEqual(even_numbers,numbers)
unittest.main()