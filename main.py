
from typing import Literal
from utils.circuit import Circuit

TYPE = Literal['GND', 'V', 'R']


# nodes: list of node labels

# components: list of tuples (label, componenent_type, start_label, end_label, value)

def main():
    nodes = ['GND', 'N01']
    components = [('V01', 'V', 'GND', 'N01', 5), ('R01', 'R', 'R03', 'GND', 1), ('R02', 'R', 'N01', 'GND', 2), ('R03', 'R', 'N01', 'R01', 3)]

    test = Circuit(nodes, components)


if __name__ == "__main__":
    main()