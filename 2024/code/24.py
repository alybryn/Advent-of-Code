DAY = 24

START = f'workspaces/Advent of Code/2024'
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

def parse(puzzle_input):
    # parse the input
    wires, gates = puzzle_input.split('\n\n')
    wires_dict = {}
    for wire in wires:
        w_name, w_value = wire.split(': ')
        wire_dict[w_name] = w_state
    gate_dict = {}
    for gate in gates:
        in1, op, in2, _, out = gate.split(' ')
        gate_dict[out] = Gate(in1, op, in2)
    return wire_dict, gate_dict

Gate = namedtuple('Gate', ['in1', 'op', 'in2'])

def wire_value(wire,wires,gates):
    if wire not in wires:
        wires[wire] = gate_value(wire,wires,gates)
    return wires[wire]

def gate_value(gate,wires,gates):
    assert gate in gates
    in1, op, in2 = gates[gate]
    match op:
        case 'AND': return wire_value(in1) and wire_value(in2)
        case 'OR': return wire_value(in1) or wire_value(in2)
        case 'XOR':
            return (not wire_value(in1) and wire_value(in2)) or (wire_value(in1) and not wire_value(in2))

def list_to_decimal(bits):
    ret=0
    for i in range(0,len(bits)):
        ret += pow(2,i) * bits[i]

def part1(parsed):
    print(parsed)
    wires,gates = parsed
    bits = []
    for z in range(0,46):
        z = 'z' + str(z) if z > 9 else 'z0' + str(z)
        bits.append(wire_value(z))
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
