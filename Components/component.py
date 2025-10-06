'''
Benjamin Smith
San Francisco State University
Copyright 2025
Rights Reserved

component.py

Sets up Component class which will be the base block upon which all other components are built
'''

import numpy as np
from Components.node import Node
from typing import Literal

TYPE = Literal['V', 'R']

class Component:
    def __init__(self, label, type : TYPE, start = None, end = None, value = 0):
        # set start and end nodes
        self._start = start
        self._end = end

        # set label for component
        self._label = label

        # set value of component
        self._value = value

        # define type of component
        self._type = type

    '''
    Return name of component
    '''
    def get_label(self):
        return self._label
    
    '''
    Return start node
    '''
    def get_start(self):
        return self._start
    
    '''
    Set start node
    '''
    def set_start(self, start):
        self._start = start

    '''
    Return end node
    '''
    def get_end(self):
        return self._end
    
    '''
    Set end node
    '''
    def set_end(self, end):
        self._end = end
    
    '''
    Returns value of component
    '''
    def get_value(self):
        return self._value
    
    '''
    Sets value of component
    '''
    def set_value(self, value):
        self._value = value

    '''
    Returns component type
    '''
    def get_type(self):
        return self._type
    
    '''
    Sets component type
    '''
    def set_type(self, type : TYPE):
        self._type = type

    '''
    Overrides __str__ function for components
    '''
    def __str__(self):
        out = self.get_label()# + '\t' + self.get_start().get_label() + '\t' + self.get_end().get_label() + '\t' + self.get_value()
        return out
