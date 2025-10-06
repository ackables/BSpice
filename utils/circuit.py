'''
Benjamin Smith
San Francisco State University
Copyright 2025
Rights Reserved

circuit.py

Construct a circuit from a list of node labels and a list of component labels, start labels, end labels, components values, and component types.

    nodes: list of node labels

    components: list of tuples (label, componenent_type, start_label, end_label, value)
'''

from Components.component import Component
from Components.node import Node
from typing import Literal

TYPE = Literal['V', 'R']

class Circuit:
    def __init__(self, nodes : list, components : list):
        self._nodes = []
        self._components = []

        for label in nodes:
            if label == 'GND':
                print(f"Creating {label} node.")
                self._nodes.append(Node(label=label, connections=None, voltage=0))
            else:
                print(f"Creating {label} node.")
                self._nodes.append(Node(label=label, connections=None, voltage=None))

        for label, type, start, end, value in components:
            print(f"Creating {label} component.")
            self._components.append(Component(label=label, type=type, start=start, end=end, value=value))

        # build circuit connections
        self.__build_connections()

    '''
    Builds connections between nodes and components. Only run at circuit object initialization.
    '''
    def __build_connections(self):
        for component in self._components:
            print(f"Building connections for {component}")
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
                # add component to connection list of node with '-' to note negative terminal 
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
    Add node to circuit

    return -1 if failed to add node
    '''
    def add_node(self, label : str, component : Component, anchor : Literal['start', 'end']):
        for node in self._nodes:
            if label == node.get_label():
                print(f"Error: Node label, \"{label}\", already in use.")
                return -1
        
        component = self.find_component(component)

        if anchor == 'start':
            component_pair = component.get_start()
        elif anchor == 'end':
            component_pair = component.get_end()
        else:
            print(f"Invalid anchor value: {anchor}\nValid anchor values: 'start' or 'end'")
            return -1
        
        # create node in between two existing components
        if label == 'GND':
            # create special ground node
            node = Node(label=label, connections=[component, component_pair], voltage=0)
        else:
            # create normal node
            node = Node(label=label, connections=[component, component_pair])
        
        self._nodes.append(node)

        # attaches node to component
        if anchor == 'start':
            component.set_start(node)
        else:
            component.set_end(node)

        # attaches node to component_pair
        if component_pair.get_start() == component:
            component_pair.set_start(node)
        else:
            component_pair.set_end(node)

    '''
    Return node with given label

    Return -1 if node not found
    '''
    def find_node(self, label : str):
        for node in self._nodes:
            if node.get_label() == label:
                return node

        #print("Error: Node not found.")    
        return -1

    '''
    Adds component to circuit

    Return -1 if fails to add
    '''
    def add_component(self, label : str, type, start_label : str, end_label : str, value):
        if label == 'GND':
            print("Error: 'GND' is a node.")
            return -1
        if self.find_component(start_label) == -1 and self.find_node(start_label) == -1:
            print("Error: start_label does not match any existing components or nodes.")
            return -1
        if self.find_component(end_label) == -1 and self.find_node(end_label) == -1:
            print("Error: end_label does not match any existing components or nodes.")
            return -1
        
        # track whether start and end points are nodes or components
        # -1 if Node
        s_type = self.find_component(start_label)
        e_type = self.find_component(end_label)

        if s_type == -1:
            start = self.find_node(start_label)
        else:
            start = self.find_component(start_label)

        if e_type == -1:
            end = self.find_node(end_label)
        else:
            end = self.find_component(end_label)

        component = Component(label=label, type=type, start=start, end=end, value=value)
        self._components.append(component)
        print(f"Added Component:\nLabel: {component.get_label()}\tType: {component.get_type()}\t\tStart: {component.get_start().get_label()}\tEnd: {component.get_end().get_label()}\tValue: {component.get_value()}")


        if s_type == -1:
            self.find_node(start_label).add_connection(component)
        if e_type == -1:
            self.find_node(end_label).add_connection(component)

    '''
    Return component with given label

    Return -1 if component not found
    '''
    def find_component(self, label : str):
        for component in self._components:
            if component.get_label() == label:
                return component

        #print("Error: Component not found.")    
        return -1
            
