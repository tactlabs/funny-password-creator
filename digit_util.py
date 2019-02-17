#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: raja

Source:
    https://stackoverflow.com/questions/2673385/how-to-generate-random-number-with-the-specific-length-in-python    
'''

# Import necessary modules
 

from random import randint

def random_4():
    return random_with_N_digits(4)

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end) 

def startpy():
    print(random_with_N_digits(4))


if __name__ == '__main__':
    startpy()