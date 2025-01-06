DAY = 23

START = f'/workspaces/Advent of Code/2024'
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

SAMPLE_ANSWER_1 = 7
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    ret = {}
    for line in puzzle_input.splitlines():
        a,b = line.split('-')
        if a not in ret:
            ret[a] = set()
        ret[a].add(b)
    return ret

def add_mutual_dict(d,a,b):
    if a not in d:
        d[a] = set()
    if b not in d:
        d[b] = set()
    d[a].add(b)
    d[b].add(a)
    return d

def count_networks(connections):
    ret = set()
    for computer,neighbors in connections.items():
        # find a third
        for neighbor in neighbors:
            for neighbors_neighbors in connections[neighbor]:
                # looking for a join, i think
                pass
    return ret

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