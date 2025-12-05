DAY = 5
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

import pathlib
import sys

SAMPLE_ANSWER_1 = 3
SAMPLE_ANSWER_2 = 14

def parse(puzzle_input):
    # parse the input
    ranges, items = puzzle_input. split('\n\n')
    ranges = [[int(r) for r in range.split('-')] for range in ranges.split()]
    items = [int(i) for i in items.split()]
    return (ranges, items)

def part1(parsed):
    print(parsed)
    fresh = []
    ranges, items = parsed
    for i in items: 
        spoiled = True
        for range in ranges:
            if range[0] <= i <= range[1]:
                spoiled = False
                break
        if not spoiled:
            fresh.append(i)
    return len(fresh)

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
