#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest
from hello import Greeter
 
class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        greeter = Greeter()
        self.assertEqual(greeter.get_message(), 'Hello world!')
 
if __name__ == '__main__':
    unittest.main()