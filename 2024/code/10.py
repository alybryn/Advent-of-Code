DAY = 10

SAMPLE_PATH = f'sample/{DAY}.txt'
DATA_PATH = f'data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]
ALL = [SAMPLE_PATH, DATA_PATH]

RUN = ONLY_SAMPLE

# --------------------------------

import pathlib
import sys

SAMPLE_ANSWER_1 = 36
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return [[int(l) for l in line.split()] for line in puzzle_input.split()]

def adjacent(point):
    vectors = [(0,-1),(0,1),(-1,0),(1,0)]
    return [(point[0]+v[0],point[1]+v[1]) for v in vectors]

def find_trailheads(map):
    ret = []
    for i in range(0, len(map)):
        for j in range(0, len(map[0])):
            if map[i][j] == 0:
                ret.append((i,j))
    return ret

def climb_trailhead(map, trailhead):
    pass

def part1(parsed):
    print(parsed)
    return parsed

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