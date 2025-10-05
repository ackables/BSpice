'''
Benjamin Smith
San Francisco State University
Copyright 2025
Rights Reserved

resitor.py

Sets up resistor component

Units in Ohms
'''

import numpy as np

from component import Component
from node import Node

class Resistor(Component):
    def __init__(self, label, start, end, value):
        super().__init__(label, start=start, end=end, value=value, type='R')
