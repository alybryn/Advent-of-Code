DAY = 11
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

SAMPLE_ANSWER_1 = 5
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    d = {}
    for line in puzzle_input.splitlines():
        device, outputs = line.split(':')
        d.update({device:[o for o in outputs.strip().split()]})
    return d

def flood(map, start, goal):
    ret = 0
    frontier = []
    frontier.append(start)
    while len(frontier) != 0:
        device = frontier.pop(0)
        for next in map.get(device):
            if next == goal:
                ret += 1
            else:
                frontier.append(next)
    return ret

def part1(parsed):
    print(parsed)
    return flood(parsed,'you','out')

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
