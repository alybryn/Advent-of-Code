DAY = 18

START = f'/home/abi/Documents/programming/Advent of Code/2024'
SAMPLE_PATH = f'{START}/sample/{DAY}.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]

RUN = ONLY_SAMPLE

# --------------------------------

from collections import deque
import pathlib
import sys

SAMPLE_ANSWER_1 = 22
SAMPLE_ANSWER_2 = None

PROBLEM_SPACE = (6,6) if ONLY_SAMPLE else (70,70)

def parse(puzzle_input):
    # parse the input
    return set([(int(i),int(j)) for line in puzzle_input.splitlines()[:1024] for i,j in line.split(',')])

class PriorityQueue:
    def __init__(self):
        pass

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
        print('this program is not taking command line arguments.')