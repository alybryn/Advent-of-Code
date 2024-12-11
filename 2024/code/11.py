DAY = 11

SAMPLE_PATH = f'sample/{DAY}.txt'
DATA_PATH = f'data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]
ALL = [SAMPLE_PATH, DATA_PATH]

RUN = ONLY_DATA

# --------------------------------

import pathlib
import sys

SAMPLE_ANSWER_1 = 55312
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return [int(num) for num in puzzle_input.split()]

# copied from Ask Python
# memoize decorator
def memoize(f):
    cache = {}
    def foo(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return foo

@memoize
def evolve(stone):
    if stone == 0:
        return [1]
    if even_digits(stone):
        return split(stone)
    return [stone * 2024]

def even_digits(stone):
    return len(str(stone)) % 2 == 0

def split(stone):
    str_stone = str(stone)
    return [int(str_stone[:len(str_stone)//2]), int(str_stone[len(str_stone)//2:])]

def part1(parsed):
    # print(parsed)
    stones = parsed
    new_stones = []
    for _ in range(0,25):
        for stone in stones:
            new_stones += evolve(stone)
        stones = new_stones
        new_stones = []
    return len(stones)

def part2(parsed):
    stones = parsed
    new_stones = []
    for _ in range(0,75):
        for stone in stones:
            new_stones += evolve(stone)
        stones = new_stones
        new_stones = []
    return len(stones)

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