DAY = 6
YEAR = 2025

START = f'/workspaces/Advent of Code/{YEAR}'
SAMPLE_PATH = f'{START}/sample/{DAY}.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]
ALL = [SAMPLE_PATH, DATA_PATH]

RUN = ONLY_SAMPLE

# --------------------------------

from operator import mul
import pathlib
from functools import reduce
import sys

SAMPLE_ANSWER_1 = 4277556
SAMPLE_ANSWER_2 = 3263827

def parse(puzzle_input):
    # parse the input
    ret =  [line for line in puzzle_input.splitlines()]
    return ret[0:-1], [o for o in ret[-1].split()]

def do_operation(operands, operator):
    if operator == '+': return sum(operands)
    else: return reduce(mul,operands)

def part1(parsed):
    values, operators = parsed
    values = [[int(i) for i in line.split()] for line in values]
    ret = 0
    for i in range(0, len(values[0])):
        nums = []
        for j in range(0, len(values)):
            nums.append(values[j][i])
        if operators[i] == '+': ret += sum(nums)
        else: ret += reduce(mul, nums)
    return ret

def part2(parsed):
    values, operators = parsed
    ret = 0
    operands = []
    for j in range(0, len(values[0])):
        nums = []
        for i in range(0, len(values)):
            nums.append(values[i][j])
        if sum([1 for x in nums if x == ' ']) == len(values):
            if operators.pop(0) == '+': ret += sum(operands)
            else: ret += reduce(mul, operands)
            operands = []
        else:
            operands.append(int(''.join(nums)))
    return ret

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
