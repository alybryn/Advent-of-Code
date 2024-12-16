DAY = 16

START = f'/workspaces/Advent of Code/2024'
SAMPLE_PATH = f'{START}/sample/{DAY}.txt'
SAMPLE_PATH_A = f'{START}/sample/{DAY}a.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH_A, SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]
ALL = [SAMPLE_PATH, DATA_PATH]

RUN = ONLY_SAMPLE

# --------------------------------

from enum import Enum
import pathlib
import sys

SAMPLE_ANSWER_1 = 7036, 11048
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return set([(i,j) for i, line in enumerate(puzzle_input.splitlines()) for j,l in enumerate(line()) if l == '#'])

class Direction(Enum):
    N = ( 0,-1)
    E = ( 1, 0)
    S = ( 0, 1)
    W = (-1, 0)

    def turn(self):
        return {Direction.N:(Direction.W,Direction.E),
        Direction.W:(Direction.S,Direction.N),
        Direction.S:(Direction.E,Direction.W),
        Direction.E:(Direction.N,Direction.S)}

def dfs(walls, ptr, facing):
    pass

def part1(parsed):
    print(parsed)
    bounds = max(parsed)
    s = (1, bounds[1]-1)
    return bounds

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