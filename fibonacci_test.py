# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 17:07:05 2022

@author: qomon
"""

import unittest
from fibonacci import fibonacci

class fubTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(fibonacci(0))
        self.assertTrue(fibonacci(8))
        self.assertFalse(fibonacci(9))
unittest.main()