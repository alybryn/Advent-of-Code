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
        ret.add(num)
    return ret

class Stones():
    def __init__(self):
        self._stones = {}
    
    def add(self, stone, n=1):
        if stone not in self._stones:
            self._stones[stone] = 0
        self._stones[stone] += n

    def count(self):
        ret = 0
        for c in self.stones.values():
            ret += c
        return ret

def evolve(stone):
    if stone == '0':
        return ['1']
    if len(stone) % 2 == 0:
        return [stone[:len(stone)//2], stone[len(stone)//2:]]
    return [str(int(stone) * 2024)]

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