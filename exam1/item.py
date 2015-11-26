# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 08:50:48 2015

@author: 97hamsah
"""

class Djur:
    #Konstruktor
    def __init__(self, color, sex):
        self.color = color
        self.sex = sex
    
    def get_color(self):
        return self.color
    
    def set_color(self, new_color):
        self.color = new_color
        
    def get_sex(self):
        return self.sex
        
    def set_sex(self, new_sex):
        self.sex = new_sex
        
class Cat(Djur):
    #klassen för katt
    def __init__(self, color, sex, tail_length):
        #konstruktor för katt
        super().__init__(color, sex)
        self.tail_length = tail_length
    
    def get_tail_lenght(self):
        return self.tail_length
        
    def set_tail_lenght(self, new_tail_length):
        self.tail_length = new_tail_length
        
    def __str__(self):
        return self.color + ";" + self.sex + ";" + self.tail_length
        
class Bird(Djur):
    #klassen för fågel
    def __init__(self, color, sex, wing_length):
        #konstruktor för fågel
        super().__init__(color, sex)
        self.wing_length = wing_length
    
    def get_wing_length(self):
        return self.wing_length
        
    def set_wing_length(self, new_wing_length):
        self.wing_length = new_wing_length
        
    def __str__(self):
        return self.color + ";" + self.sex + ";" + self.wing_length
        
        
        