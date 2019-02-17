#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: raja

Source:
    http://www.manythings.org/vocabulary/lists/c/words.php?f=adjectives_for_people.
    https://www.enchantedlearning.com/wordlist/adjectivesforpeople.shtml

    https://stackoverflow.com/questions/2673385/how-to-generate-random-number-with-the-specific-length-in-python

'''

# Import necessary modules
import adj_reader as adr
import digit_util as du
import name_reader as nr
 

def get_password(username = None):

    adjective = adr.get_random_adj()
    digit = du.random_4()

    if(username is None):
        username = nr.get_random_name()

    password = adjective + str(username) + str(digit)

    #print(adjective)

    return password

def startpy():

    #adjectives = adr.get_adjective_list()
    #print(adjectives)
    
    passw = get_password()
    print(passw)  

if __name__ == '__main__':
    startpy()