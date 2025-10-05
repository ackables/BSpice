'''
Benjamin Smith
San Francisco State University
Copyright 2025
Rights Reserved

ground.py

Sets up ground component

Units in Volts
'''

from component import Component
from node import Node

class Ground(Component):
    def __init__(self, end, label = 'GND'):
        super().__init__(label, end=end, value=0, type='GND')


    

    