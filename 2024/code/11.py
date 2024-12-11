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
    ret = Stones()
    for num in puzzle_input.split():
        ret.add(int(num))

class Stones():
    def __init__(self, stones):
        self.stones = {}
    
    def add(self, stone):
        if stone not in self.stones:
            self.stones[stone] = 0
        self.stones[stone] += 1
    
    def count(self):
        ret = 0
        for c in self.stones.values():
            ret += c
        return ret

def evolve(stone):
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        return split(stone)
    return [stone * 2024]

def split(stone):
    str_stone = str(stone)
    return [int(str_stone[:len(str_stone)//2]), int(str_stone[len(str_stone)//2:])]

def part1(parsed):
    # print(parsed)
    stones = parsed
    cache = {}
    new_stones = []
    for _ in range(0,25):
        for stone in stones:
            if stone not in cache:
                cache[stone] = evolve(stone)
            new_stones += cache[stone]
        stones = new_stones
        new_stones = []
    return len(stones)

def part2(parsed):
    stones = parsed
    cache = {}
    new_stones = []
    for _ in range(0,75):
        for stone in stones:
            if stone not in cache:
                cache[stone] = evolve(stone)
            new_stones += cache[stone]
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