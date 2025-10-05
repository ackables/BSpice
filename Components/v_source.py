'''
Benjamin Smith
San Francisco State University
Copyright 2025
Rights Reserved

v_source.py

Sets up voltage source component

Units in Volts
'''

import numpy as np

from component import Component
from node import Node

class v_source(Component):
    def __init__(self, label, start, end, value):
        super().__init__(label, start=start, end=end, value=value, type='V')
