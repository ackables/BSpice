'''
Benjamin Smith
San Francisco State University
Copyright 2025
Rights Reserved

circuit.py

Construct a circuit from a list of node labels and a list of component labels
'''

from Components.component import Component
from Components.node import Node

class Circuit:
    def __init__(self, nodes : list, components : list):
        self._nodes = []
        self._components = []

        for label in nodes:
            self._nodes.append(Node(label=label))

        for label, start, end, value, type in components:
            self._components.append(Component(label=label, start=start, end=end, value=value, type=type))

    '''
    Inserts node between components
    '''
    def insert_node(self, c1 : Component, c2 : Component):
        if c1.get_start() == c2.get_start() or c1.get_start() == c2.get_end() or c1.get_end() == c2.get_start() or c1.get_end() == c2.get_end():
            print("Error: Components already connected to same node")