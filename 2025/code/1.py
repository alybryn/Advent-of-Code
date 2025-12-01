DAY = 1
YEAR = 2025

START = f'/workspaces/Advent of Code/{YEAR}'
SAMPLE_PATH = f'{START}/sample/{DAY}.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]
ALL = [SAMPLE_PATH, DATA_PATH]

RUN = ONLY_DATA

# --------------------------------

import pathlib
import sys

SAMPLE_ANSWER_1 = 3
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return list(map(list, zip([line[0] for line in puzzle_input.split()],[int(line[1:]) for line in puzzle_input.split()])))

def over_rotation_fix(num):
    fixes = 0
    while num > 99:
        num -= 100
        fixes += 1
    while num < 0:
        num += 100
        fixes += 1
    return (num, fixes)

def part1(parsed):
    position = 50
    times_at_zero = 0
    for rotation in parsed:
        dir, distance = rotation
        # plus direction
        if dir == 'R': position = over_rotation_fix(position + distance)[0]
        # minus direction
        else: position = over_rotation_fix(position - distance)[0]
        if position == 0: times_at_zero += 1
    return times_at_zero

def part2(parsed):
    position = 50
    times_at_zero = 0
    for rotation in parsed:
        dir, distance = rotation
        # plus direction
        if dir == 'R':
            # correction = over_rotation_fix(position+distance)
            for _ in range(0, distance):
                position += 1
                if position == 100:
                    position = 0
                    times_at_zero += 1
        # minus direction
        else:
            # correction = over_rotation_fix(position-distance)
            for _ in range(0, distance):
                position -= 1
                if position == -1:
                    position = 99
                if position == 0:
                    times_at_zero += 1
        # position = correction[0]
        # times_at_zero += correction[1]
    return times_at_zero

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