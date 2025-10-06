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
    Return terminal of component another component or node is connected to

    Return:
        '-' for start terminal
        '+' for end terminal
        -1 if fail
    '''
    def get_terminal(self, reference):
        if not (isinstance(reference, Node) or isinstance(reference, Component)):
            print("Error: Please provide a Node or Component object as argument.")
            return -1
        else:
            if self.get_start().get_label() == reference.get_label():
                return '-'
            elif self.get_end().get_label() == reference.get_label():
                return '+'
            else:
                print(f"Error: {reference.get_label()} is not connected to {self.get_label()}.")
                return -1
    
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
        print(f"{self.get_label()} start set to {start.get_label()}")

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
        print(f"{self.get_label()} end set to {end.get_label()}")
    
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
