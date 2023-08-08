#!/usr/bin/python
# -*- coding: utf-8 -*-

# run with pytest

import unittest
from peatmoss_transformers_test import main

class Test(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main.from_import(), 0)

if __name__ == '__main__':
    unittest.main()