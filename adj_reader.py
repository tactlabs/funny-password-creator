#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: raja

Source:
    https://www.enchantedlearning.com/wordlist/adjectivesforpeople.shtml
'''

# Import necessary modules
import os
import random


def get_current_location():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path    

def read_adjectives():
    f = open(get_current_location() + '/' + 'adjectives.txt')

    for line in f.readlines():
        print(line.strip())

def get_random_adj():
    return random.choice(get_adjective_list())

def get_adjective_list():
    f = open(get_current_location() + '/' + 'adjectives.txt')

    adj_list = []
    for line in f.readlines():
        #print(line.strip())        
        for item in line.split(','):
            
            # if already in list, skip it
            if(item in adj_list):
                continue

            # if - is in the list, skip it
            if('-' in item):
                continue

            # if more than 8 characters, skip it
            if(len(item) > 8):
                continue

            adj_list.append(item)

    #print(adj_list)

    return adj_list    

if __name__ == '__main__':
    #read_adjectives()
    get_adjective_list()