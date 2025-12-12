DAY = 12
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

SAMPLE_ANSWER_1 = 2
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    present_dict = {}
    blocks = puzzle_input.split('\n\n')
    for i in range(6):
        present = [[c == '#' for c in b.split()] for b in blocks[i].split()[1:]]
        present_dict.update({i:present})
    # 4x4: 0 0 0 0 2 0
    areas = []
    for line in blocks[-1].splitlines():
        area, presents = line.split(': ')
        area = tuple([a for a in area.split('x')])
        presents = presents.split()
        areas.append((area,presents))
    return present_dict, areas

def permute(p):
    ret = {p,flip(p)}
    for _ in range(3):
        p = rotate(p)
        ret.add(p)
        ret.add(flip(p))
    return ret

def flip(p):
    return ((p[0][2],p[0][1],p[0][0]),
            (p[1][2],p[1][1],p[1][0]),
            (p[2][2],p[2][1],p[2][0]))

def rotate(p):
    return ((p[2][0],p[1][0],p[0][0]),
            (p[2][1],p[1][1],p[0][1]),
            (p[2][2],p[1][2],p[0][2]))
def part1(parsed):
    print(parsed)
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
