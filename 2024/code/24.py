DAY = 24

START = f'/workspaces/Advent-of-Code/2024'
SAMPLE_PATH = f'{START}/sample/{DAY}.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]
ALL = [SAMPLE_PATH, DATA_PATH]

RUN = ONLY_SAMPLE

# --------------------------------

from collections import namedtuple
import pathlib
import sys

SAMPLE_ANSWER_1 = 2024
SAMPLE_ANSWER_2 = None

WIRES = {}
GATES = {}

def parse(puzzle_input):
    # parse the input
    wires, gates = puzzle_input.split('\n\n')
    global WIRES
    for wire in wires.splitlines():
        w_name, w_state = wire.split(': ')
        WIRES[w_name] = w_state
    global GATES
    for gate in gates.splitlines():
        in1, op, in2, _, out = gate.split(' ')
        GATES[out] = Gate(in1, op, in2)
    return

Gate = namedtuple('Gate', ['in1', 'op', 'in2'])

def wire_value(wire):
    global WIRES
    if wire not in WIRES:
        WIRES[wire] = gate_value(wire)
    return WIRES[wire]

def gate_value(gate):
    if gate not in GATES:
        return 0
    in1, op, in2 = GATES[gate]
    match op:
        case 'AND': return wire_value(in1) and wire_value(in2)
        case 'OR': return wire_value(in1) or wire_value(in2)
        case 'XOR':
            return (not wire_value(in1) and wire_value(in2)) or (wire_value(in1) and not wire_value(in2))

def list_to_decimal(bits):
    print(bits)
    ret = 0
    for i in range(0,len(bits)):
        ret += pow(2,i) * bits[i]
    return ret

def part1(parsed):
    print(parsed)
    bits = []
    for z in range(0,46):
        z = 'z' + str(z) if z > 9 else 'z0' + str(z)
        bits.append(1) if wire_value(z) else bits.append(0)
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
