# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 08:50:13 2015

@author: 97hamsah
"""
from item import *

class Model:
    
    def __init__(self):
        self.lista = []
    
        
        
    def add_cat(self, color, sex, tail_length):
        self.cat = Cat(color, sex, tail_length)
        self.lista.append(self.cat)
        
    def add_bird(self, color, sex, wing_length):
        self.bird = Bird(color, sex, wing_length)
        self.lista.append(self.bird)
        self.lista.append("Swag")
    
    
        
        