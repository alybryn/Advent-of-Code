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
import sys

SAMPLE_ANSWER_1 = 6
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    towels, patterns = puzzle_input.split("\n\n")
    towels = set([t for t in towels.split(", ")])
    max_len =0
    for t in towels:
        if len(t) > max_len:
            max_len = len(t)
    patterns = patterns.splitlines()
    return towels, patterns, max_len

DP = {'':1}
def is_design_possible(towels, design, max_len):
    if design not in DP:
        c = 0
        matches = get_towels(towels,design[:max_len])
        if matches:
            for match in matches:
                if is_design_possible(towels,design.removeprefix(match),max_len):
                    c += 1
        DP[design] = c
    return DP[design]

GT = {}
def get_towels(towels, design):
    if design not in GT:
        ret = []
        for sl in range(0,len(design)+1):
            if design[:sl] in towels:
                ret.append(design[:sl])
        GT[design] = ret
    return GT[design]

def part1(parsed):
    # print(parsed)
    towels, designs, max_len = parsed
    c = 0
    for design in designs:
        print(design)
        if is_design_possible(towels, design, max_len):
            c += 1
    return c

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