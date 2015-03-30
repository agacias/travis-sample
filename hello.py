#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
 
class Greeter:
    def __init__(self):
        self.message = 'Hello world!'
    
    def get_message(self):
        return self.message


def main(argv=None):
	g = Greeter()
	print g.get_message()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
