#!/usr/bin/env python3

from string import ascii_letters, digits
from itertools import chain
from random import choice
import os

def create_uid(n=9):
   '''Génère une chaîne de caractères alétoires de longueur n
   en évitant 0, O, I, l pour être sympa.'''
   chrs = [ c for c in chain(ascii_letters,digits)
                        if c not in '0OIl'  ]
   return ''.join( ( choice(chrs) for i in range(n) ) ) 
