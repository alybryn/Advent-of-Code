DAY = 2
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
import re

SAMPLE_ANSWER_1 = 1227775554
SAMPLE_ANSWER_2 = 4174379265

def parse(puzzle_input):
    # parse the input
    return [[int(i) for i in id_range.split("-")] for id_range in puzzle_input.split(",")]

def validate_1(sku):
    s_sku = str(sku)
    hl = len(s_sku)//2
    return s_sku[:hl] == s_sku[hl:]

def validate_2(sku):
    s_sku = str(sku)
    for pl in range(1,len(s_sku)//2 +1):
        temp = s_sku[:pl]
        pattern = re.compile(f'^({temp})*$')
        m = re.match(pattern, s_sku)
        if m: return sku
    return False

def part1(parsed):
    ret = []
    for r in parsed:
        for i in range(r[0], r[1]+1):
            if validate_1(i): ret.append(i)
    return sum(ret)

def part2(parsed):
    ret = []
    for r in parsed:
        for i in range(r[0], r[1]+1):
            if validate_2(i): ret.append(i)
    return sum(ret)

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
