DAY = 7
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

SAMPLE_ANSWER_1 = 21
SAMPLE_ANSWER_2 = 40

def parse(puzzle_input):
    # parse the input
    return [[l for l in line] for line in puzzle_input.splitlines()]

# def get_splitter_locs(map):
#     ret = []
#     for i in range(0, len(map[0])):
#         for j in range(0, len(map)):
#             if map[i][j] == '^':
#                 ret.append((i,j))
#     return ret

def print_lvl(map, beams):
    p = ''
    for i in range(0, len(map)):
        if i in beams:
            p += '|'
        else:
            p += map[i]
    print(p)

def part1(parsed):
    ret = 0
    start= parsed[0].index('S')
    beams = {start}
    for l in parsed[1:]:
        new_beams = set()
        for b in beams:
            if l[b] == '^':
                new_beams.add(b-1)
                new_beams.add(b+1)
                ret += 1
            else:
                new_beams.add(b)
        beams = new_beams
    return ret

def part2(parsed):
    ret = 1
    start= parsed[0].index('S')
    beams = [start]
    for l in parsed[1:]:
        new_beams = []
        for b in beams:
            if l[b] == '^':
                new_beams.append(b-1)
                new_beams.append(b+1)
                ret += 1
            else:
                new_beams.append(b)
        beams = new_beams
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
