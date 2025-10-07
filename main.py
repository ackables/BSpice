
from typing import Literal
from utils.circuit import Circuit

TYPE = Literal['V', 'R']


# nodes: list of node labels

# components: list of tuples (label, componenent_type, start_label, end_label, value)

def main():
    nodes = ['GND', 'N01']
    components = [('V01', 'V', 'GND', 'N01', 5), ('R01', 'R', 'GND', 'R03', 1), ('R02', 'R', 'GND', 'N01', 2), ('R03', 'R', 'N01', 'R01', 3)]

    test = Circuit(nodes, components)

    for node in test._nodes:
        connections_list = []
        for connections in node.get_connections():
            terminal = connections.get_terminal(node)
            connections_list.append(terminal + connections.get_label())
        print(f"Label: {node.get_label()}\tConnections: {connections_list}\tVoltage: {node.get_voltage()}")

    for component in test._components:
        print(f"Label: {component.get_label()}\tType: {component.get_type()}\t\tStart: {component.get_start().get_label()}\tEnd: {component.get_end().get_label()}\tValue: {component.get_value()}")

    # new nodes must be added before new components that connect to those nodes are added
    test.add_node('N02', 'R01', 'end')
    test.add_component('R04', 'R', 'GND', 'N02', 4)

    for node in test._nodes:
        connections_list = []
        for connections in node.get_connections():
            terminal = connections.get_terminal(node)
            connections_list.append(terminal + connections.get_label())
        print(f"Label: {node.get_label()}\tConnections: {connections_list}\tVoltage: {node.get_voltage()}")

    for component in test._components:
        print(f"Label: {component.get_label()}\tType: {component.get_type()}\t\tStart: {component.get_start().get_label()}\tEnd: {component.get_end().get_label()}\tValue: {component.get_value()}")

    # test Component.flip()

    # test.find_component("R01").flip()

    # for node in test._nodes:
    #     connections_list = []
    #     for connections in node.get_connections():
    #         terminal = connections.get_terminal(node)
    #         connections_list.append(terminal + connections.get_label())
    #     print(f"Label: {node.get_label()}\tConnections: {connections_list}\tVoltage: {node.get_voltage()}")

    # for component in test._components:
    #     print(f"Label: {component.get_label()}\tType: {component.get_type()}\t\tStart: {component.get_start().get_label()}\tEnd: {component.get_end().get_label()}\tValue: {component.get_value()}")

    # test Node.set_kcl()
    neg, pos, recursive = test.find_node('N02').set_kcl()
    if recursive == True:
        print("Recursive call")

    for node in test._nodes:
        connections_list = []
        for connections in node.get_connections():
            terminal = connections.get_terminal(node)
            connections_list.append(terminal + connections.get_label())
        print(f"Label: {node.get_label()}\tConnections: {connections_list}\tVoltage: {node.get_voltage()}")

    for component in test._components:
        print(f"Label: {component.get_label()}\tType: {component.get_type()}\t\tStart: {component.get_start().get_label()}\tEnd: {component.get_end().get_label()}\tValue: {component.get_value()}")


if __name__ == "__main__":
    main()