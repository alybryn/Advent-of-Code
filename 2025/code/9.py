DAY = 9
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

SAMPLE_ANSWER_1 = 50
SAMPLE_ANSWER_2 = 24

def parse(puzzle_input):
    # parse the input
    points = [to_tuple([int(l) for l in line.split(',')]) for line in puzzle_input.split()]
    lines = []
    for i in range(0, len(points)-1):
        lines.append(points[i],points[i+1])
    lines.append(points[-1],points[0])
    boxes = []
    while len(points) != 0:
        t1 = points.pop()
        for t2 in points:
            boxes.append((t1,t2))
    return boxes, lines

def to_tuple(two_item_list):
    assert(len(two_item_list)==2)
    return (two_item_list[0],two_item_list[1])

def area(t1, t2):
    return (abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1)

def part1(parsed):
    boxes = parsed[0]
    big = 0
    for box in boxes:
        a = area(box[0], box[1])
        if a > big: big = a
    return big

def part2(parsed):
    boxes,points = parsed
    big = 0
    for box in boxes:
        a = area(box[0], box[1])
        if a > big: big = a
    return big

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
