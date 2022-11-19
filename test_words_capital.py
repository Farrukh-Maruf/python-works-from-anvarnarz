# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 19:12:20 2022

@author: qomon
"""

import unittest
from words_capital import words
class wordsTest(unittest.TestCase):
    def test_words(self):
        x = ['sen bilan men', 'men bilan sen']
        format_name=words(x)
        equal_name= ['Sen Bilan Men', 'Men Bilan Sen']
        self.assertEqual(format_name,equal_name)
unittest.main()