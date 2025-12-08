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
SAMPLE_ANSWER_2 = 25272

def parse(puzzle_input):
    # parse the input
    boxes = [to_tuple([int(l) for l in line.split(',')]) for line in puzzle_input.split()]
    # for each junction box, find the distance to all other junction boxes
    # store in dict {distance:(b1,b2)}
    distances = {}
    while len(boxes) != 0:
        box = boxes.pop()
        for junction in boxes:
            dist = sld(box,junction)
            distances.update({dist:(box,junction)})
    return distances

def sld(b1, b2):
    return sqrt((b1[0]-b2[0])**2+(b1[1]-b2[1])**2+(b1[2]-b2[2])**2)

def to_tuple(three_item_list):
    assert(len(three_item_list)==3)
    return (three_item_list[0],three_item_list[1],three_item_list[2])

def extention_cable(c1,c2, circuits):
    for c in circuits:
        if c1 in c: c1 = c
        if c2 in c: c2 = c
    if c1 != c2:
        if not isinstance(c1,list): c1 = [c1]
        else: circuits.remove(c1)
        if not isinstance(c2,list): c2 = [c2]
        else: circuits.remove(c2)

        circuits.append(c1 + c2)

def part1(parsed):
    distances = parsed.copy()
    # build circuits
    circuits = []
    for _ in range(0,10):
        # pop the shortest connection
        m = distances.pop(min(distances))
        # locate each box's circuit, if extant
        # default is a single box circuit
        c1 = m[0]
        c2 = m[1]
        extention_cable(c1,c2,circuits)
    circuits = [sum([1 for _ in c]) for c in circuits]
    circuits.sort()
    circuits.reverse()
    ret = 1
    for c in circuits[:3]:
        ret *= c
    return ret

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
