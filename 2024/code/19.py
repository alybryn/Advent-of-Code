DAY = 19

START = f'/workspaces/Advent of Code/2024'
SAMPLE_PATH = f'{START}/sample/{DAY}.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]
ALL = [SAMPLE_PATH, DATA_PATH]

RUN = ONLY_SAMPLE

# --------------------------------

import pathlib
import re
import sys

SAMPLE_ANSWER_1 = 6
SAMPLE_ANSWER_2 = 16

def parse(puzzle_input):
    # parse the input
    towels, patterns = puzzle_input.split("\n\n")
    towels = [t for t in towels.split(", ")]
    designs = patterns.splitlines()
    ret = []
    for design in designs:
        ret.append(is_design_possible(towels, design))
    return ret


DP = {'':1}
def is_design_possible(towels, design):
    if design not in DP:
        c = 0
        for new_design in remove_one_towel(towels,design):
            p = is_design_possible(towels, new_design)
            if p:
                c = p+1
        DP[design] = c
    return DP[design]

GT = {}
def remove_one_towel(towels, design):
    if design not in GT:
        ret = []
        for towel in towels:
                if re.match(towel,design):
                    ret.append(design.removeprefix(towel))
        GT[design] = ret
    return GT[design]

def part1(parsed):
    # print(parsed)
    return sum([1 for p in parsed if p != 0])

def part2(parsed):
    print(parsed)
    return sum(parsed)

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