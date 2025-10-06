'''
Benjamin Smith
San Francisco State University
Copyright 2025
Rights Reserved

node.py

Sets up Node class which will define the connections between >2 components and/or define points where voltage wrt GND will be calculated
'''

import numpy as np
from typing import Iterable, Optional, List

class Node:
    def __init__(self, label, connections: Optional[List] = None, voltage = None):
        # name of node
        self._label = label
        # list of connected components
        self._connections = connections if connections is not None else []
        # node voltage
        self._voltage = voltage

    '''
    Return name of node
    '''
    def get_label(self):
        return self._label

    '''
    Return list of components connected to the node
    '''
    def get_connections(self):
        return self._connections
    
    '''
    Add a single component or list of components to the connections list
    '''
    def add_connection(self, component):
        # if component is iterable and is not a string
        if isinstance(component, Iterable) and not isinstance(component, (str, bytes)):
            # extend with component list
            self._connections.extend(component)
            print(f"{component.get_label()} connected to {self.get_label()}.")
        else:
            # append with single component
            self._connections.append(component)
            print(f"{component.get_label()} connected to {self.get_label()}.")

    '''
    Return node voltage
    '''
    def get_voltage(self):
        return self._voltage
    
    '''
    Set voltage of node
    '''
    def set_voltage(self, voltage):
        self._voltage = voltage

    '''
    Overrides __str__ function for nodes
    '''
    def __str__(self):
        out = self.get_label()# + '\t' + self.get_voltage() + '\t' + self.get_connections
        return out