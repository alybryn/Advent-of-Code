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
    return ret, find_all_networks(ret)

def find_all_networks(connections):
    ret = set()
    for computer,neighbors in connections.items():
        for neighbor in neighbors:
            for third in connections[neighbor].intersection(neighbors):
                network = [computer,neighbor,third]
                network.sort()
                ret.add(tuple(network))
            for n in connections[neighbor]:
                for deeper in connections[n]:
                    if deeper == computer:
                        network = [computer,neighbor,n]
                        network.sort()
                        ret.add(tuple(network))
    return ret

def print_network(network):
    l = list(network)
    l.sort()
    print('\n'.join([print_password(n) for n in l]))

def print_password(network):
    return ','.join(network)

def part1(parsed):
    # print(parsed)
    _, nets = parsed
    filtered = [n for n in nets if sum([1 for y in n if y.startswith('t')])]
    return len(filtered)

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