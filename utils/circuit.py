'''
Benjamin Smith
San Francisco State University
Copyright 2025
Rights Reserved

circuit.py

Construct a circuit from a list of node labels and a list of component labels, start labels, end labels, components values, and component types.

    nodes: list of node labels

    components: list of tuples (label, start_label, end_label, value, component_type)
'''

from Components.component import Component
from Components.node import Node

class Circuit:
    def __init__(self, nodes : list, components : list):
        self._nodes = []
        self._components = []

        for label, connections in nodes:
            self._nodes.append(Node(label=label))

        for label, start, end, value, type in components:
            self._components.append(Component(label=label, start=start, end=end, value=value, type=type))

        # build circuit connections
        self.__build_connections()

    '''
    Builds connections between nodes and components. Only run at circuit object initialization.
    '''
    def __build_connections(self):
        for component in self._components:
            # search for nodes using start and end labels of components
            s_label = self.find_node(component.get_start())
            e_label = self.find_node(component.get_end())

            # if start is not an existing node
            if s_label == -1:
                # check if label belongs to a component
                s_label = self.find_component(component.get_start())
                # if start is not an existing component
                if s_label == -1:
                    print(f"Error: Start of {component.get_label()} does not exist")
                # if start is an existing component
                else:
                    # set start to existing component
                    component.set_start(s_label)
            # if start is an existing node
            else:
                # set start to node with given node label
                component.set_start(s_label)
                # add component to connection list of node
                s_label.add_connection(component)
            
            # if end is not an existing node
            if e_label == -1:
                # check if end is an existing component
                e_label = self.find_component(component.get_end())
                # if end is not an existing component
                if e_label == -1:
                    print(f"Error: End of {component.get_label()} does not exist")
                # if end is an existing component
                else:
                    # set end to existing component
                    component.set_end(e_label)
            # if end is an existing node
            else:
                # set end to node with given node label
                component.set_end(e_label)
                # add component to connection list of node
                e_label.add_connection(component)

    '''
    Inserts node between components

    return -1 if failed to add node
    '''
    def add_node(self, label : str):
        for node in self._nodes.get_label():
            if label == node:
                print(f"Error: Node label, \"{label}\", already in use.")
                return -1
        
        self._nodes.append(Node(label=label))

    '''
    Return node with given label

    Return -1 if node not found
    '''
    def find_node(self, label : str):
        for node in self._nodes:
            if node.get_label() == label:
                return node
            
        return -1

    '''
    Return component with given label

    Return -1 if component not found
    '''
    def find_component(self, label : str):
        for component in self._nodes:
            if component.get_label() == label:
                return component
            
        return -1
            
