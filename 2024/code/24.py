DAY = 24

START = f'/workspaces/Advent of Code/2024'
SAMPLE_PATH = f'{START}/sample/{DAY}.txt'
SAMPLE_PATH_A = f'{START}/sample/{DAY}a.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH, SAMPLE_PATH_A]
ONLY_DATA = [DATA_PATH]
ALL = [SAMPLE_PATH, DATA_PATH]

RUN = ONLY_SAMPLE

# --------------------------------

from collections import namedtuple
import pathlib
import sys

SAMPLE_ANSWER_1 = 4, 2024
SAMPLE_ANSWER_2 = None

INITIAL_WIRES = {}
WIRES = {}
GATES = {}

def parse(puzzle_input):
    # parse the input
    wires, gates = puzzle_input.split('\n\n')
    global INITIAL_WIRES,WIRES,GATES
    INITIAL_WIRES = {}
    WIRES = {}
    GATES = {}
    for wire in wires.splitlines():
        w_name, w_state = wire.split(': ')
        INITIAL_WIRES[w_name] = True if int(w_state) else False
    for gate in gates.splitlines():
        in1, op, in2, _, out = gate.split(' ')
        GATES[out] = Gate(in1, op, in2)
    return

Gate = namedtuple('Gate', ['in1', 'op', 'in2'])

def wire_value(wire):
    global WIRES
    if wire not in INITIAL_WIRES and wire not in GATES:
        return False
    if wire not in WIRES:
        if wire in GATES:
            WIRES[wire] = gate_value(wire)
        elif wire in INITIAL_WIRES:
            return INITIAL_WIRES[wire]
    return WIRES[wire]

def gate_value(gate):
    in1, op, in2 = GATES[gate]
    match op:
        case 'AND':
            ret = wire_value(in1) and wire_value(in2)
            print(f'{in1} and {in2} = {ret}')
            return ret
        case 'OR': 
            ret = wire_value(in1) or wire_value(in2)
            print(f'{in1} or {in2} = {ret}')
            return ret
        case 'XOR':
            ret =  xor(wire_value(in1),wire_value(in2))
            print(f'{in1} xor {in2} = {ret}')
            return ret

def xor(a,b):
    return (a and not b) or (b and not a)

def list_to_decimal(bits):
    print(bits)
    ret = 0
    for i in range(0,len(bits)):
        ret += pow(2,i) * bits[i]
    return ret

class WireMachine:
    def __init__(self,initial_wires, gates):
        self._initial_wires = initial_wires
        self._gates = gates
        self._in_size = int(max(self._initial_wires.keys())[1:])
        self._out_size = self._in_size + 1

    def wire_value(self,name):
        pass

    def gate_value(self,name):
        pass

    def addition(self):
        return self.x_value() + self.y_value()

    def x_value(self):
        bits = [x for x in self._initial_wires.keys() if x.startswith('x')]
        bits.sort()
        return list_to_decimal(bits)
    
    def y_value(self):
        bits = [y for y in self._initial_wires.keys() if y.startswith('y')]
        bits.sort()
        return list_to_decimal(bits)
    
    def z_value(self):
        bits = []
        for z in range(0,self._out_size):
            z = 'z' + str(z) if z > 9 else 'z0' + str(z)
            bits.append(1) if self.wire_value(z) else bits.append(0)
        return list_to_decimal(bits)

def part1(parsed):
    print(INITIAL_WIRES)
    bits = []
    for z in range(0,99):
        z = 'z' + str(z) if z > 9 else 'z0' + str(z)
        if z in ['z02','z03']: print(z)
        bits.append(1) if wire_value(z) else bits.append(0)
    """
    for name, state in WIRES.items():
        value, is_set = state
        print(f'{name}: was set?:{is_set}. Value: {value}')
    """
    return list_to_decimal(bits)

def part2(parsed):
    return 0

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

def run(path):
    print(f'{path}')
    puzzle_input = pathlib.Path(path).read_text().strip()

    solutions = solve(puzzle_input)
    print('\n'.join(str(solution) for solution in solutions))

if __name__ == "__main__":
    for path in RUN:
        run(path)
    for path in sys.argv[1:]:
        run(path)
