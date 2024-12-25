DAY = 25

START = f'/workspaces/Advent-of-Code/2024'
SAMPLE_PATH = f'{START}/sample/{DAY}.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]
ALL = [SAMPLE_PATH, DATA_PATH]

RUN = ALL

# --------------------------------

import pathlib
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    keys_and_locks = puzzle_input.split('\n\n')
    keys = [shape_of(k[6:35].splitlines()) for k in keys_and_locks if k.startswith('.....')]
    locks = [shape_of(l[6:35].splitlines()) for l in keys_and_locks if l.startswith('#####')]

    return keys, locks

def shape_of(searching):
    ret = [0,0,0,0,0]
    for i in range(0,5):
        for j in range(0,5):
            if searching[i][j] == '#':
                ret[j] += 1
    return ret

def are_compatable(lock,key):
    for l,k in zip(lock,key):
        if k+l >5: return False
    return True

def part1(parsed):
    print(parsed)
    keys, locks = parsed
    c = 0
    for lock in locks:
        for key in keys:
            if are_compatable(lock, key):
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