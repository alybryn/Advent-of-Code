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

    @property
    def count(self):
        ret = 0
        for c in self._stones.values():
            ret += c
        return ret
    
    @property
    def items(self):
        return self._stones.items()
    
    def __repr__(self):
        ret = ''
        for key in self._stones.keys():
            ret += f'{self._stones[key]} stones called {key}, '
        return ret.strip(', ')

def evolve(stone):
    if stone == '0' or stone == '':
        return ['1']
    if len(stone) % 2 == 0:
        return [stone[:len(stone)//2], stone[len(stone)//2:].lstrip('0')]
    return [str(int(stone) * 2024)]

def blink(times, input_stones):
    stones = input_stones
    cache = {}
    new_stones = Stones()
    for _ in range(0, times):
        for stone, number in stones.items:
            if stone not in cache:
                cache[stone] = evolve(stone)
            for s in cache[stone]:
                new_stones.add(s,number)
        stones = new_stones
        new_stones = Stones()
    return stones.count

def part1(parsed):
    # print(parsed)
    return blink(25, parsed)

def part2(parsed):
    return blink(75, parsed)

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