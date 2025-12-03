DAY = 3
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

SAMPLE_ANSWER_1 = 357
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return [line for line in puzzle_input.split()]

def max_digit(s):
    m = 0
    for i in range(0, len(s)):
        c = int(s[i])
        if c > m: m = c
    return m

def concatonator(l):
    s = ''
    for d in l:
        s += str(d)
    return int(s)

def part1(parsed):
    ret = 0
    for bank in parsed:
        biggest = max_digit(bank[:-1])
        i = bank.find(str(biggest))
        second = max_digit(bank[i+1:])
        ret += int(f'{biggest}{second}')
    return ret

# same thing but twelve digits
def part2(parsed):
    ret = 0
    for bank in parsed:
        found_offset = 0
        reserve_offset = -11
        number = []
        while reserve_offset < 0:
            number.append(max_digit(bank[found_offset:reserve_offset]))
            found_offset += bank[found_offset:reserve_offset].find(str(number[-1])) + 1
            reserve_offset += 1
        ret += concatonator(number)
    return ret

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
