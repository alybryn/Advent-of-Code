DAY = 8
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
from math import sqrt
import sys

SAMPLE_ANSWER_1 = 40
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return [to_tuple([int(l) for l in line.split(',')]) for line in puzzle_input.split()]

def sld(b1, b2):
    return sqrt((b1[0]-b2[0])**2+(b1[1]-b2[1])**2+(b1[2]-b2[2])**2)

def to_tuple(three_item_list):
    assert(len(three_item_list)==3)
    return (three_item_list[0],three_item_list[1],three_item_list[2])

def part1(parsed):
    print(parsed)
    # for each junction box, find the distance to all other junction boxes
    # store in dict {distance:(b1,b2)}
    # build circuits
    return 0

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
