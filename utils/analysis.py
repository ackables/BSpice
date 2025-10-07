'''
Benjamin Smith
San Francisco State University
Copyright 2025
Rights Reserved

analysis.py

Analysis methods that can be run on Circuit objects
'''

import numpy as np
import random
from utils.circuit import Circuit

'''
Runs nodal analysis to compute voltages at all Nodes in a Circuit.

Voltages at each Node updated with correct voltages.

Returns -1 if failed
'''
def nodal_analysis(self : Circuit):
    '''
    At each node in the circuit, Kirchhoff's Current Law must hold:
        i_in = sum(i_out)
    
    Analysis begins at GND where voltage known to be 0

    If GND is directly connected to a voltage source, the voltage at the opposite end of the voltage source is +/- the value of the voltage source
    If a voltage source is between two non-GND nodes, the end_node.get_voltage() = voltage.get_value() + start_node.get_voltage()

    Setting component directions:
        Each node besides the GND node must be connected to at least 1 component end and at least 1 component start.
        If a node is only connected to one type of component side, flip the first component(will automatically flip subsequent components until a node is reached.)
    '''

    current = self.find_node('GND')

    if current == -1:
        print("Error: Please place a GND node before analysis.")
        return -1
    
    for node in self._nodes():
        # list of current node positive and negative components
        curr_neg, curr_pos, recursive = node.set_kcl()

