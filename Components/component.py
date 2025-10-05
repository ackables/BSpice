'''
Benjamin Smith
San Francisco State University
Copyright 2025
Rights Reserved

component.py

Sets up Component class which will be the base block upon which all other components are built
'''

import numpy as np

from node import Node

class Component:
    def __init__(self, label, start = None, end = None, value = 0, type = None):
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
    Return end node
    '''
    def get_end(self):
        return self._end
    
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
    Overrides __str__ function for components
    '''
    def __str__(self):
        out = self.get_label()# + '\t' + self.get_start().get_label() + '\t' + self.get_end().get_label() + '\t' + self.get_value()
        return out
