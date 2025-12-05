DAY = 5
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

SAMPLE_ANSWER_1 = 3
SAMPLE_ANSWER_2 = 14

def parse(puzzle_input):
    # parse the input
    ranges, items = puzzle_input. split('\n\n')
    ranges = [[int(r) for r in range.split('-')] for range in ranges.split()]
    items = [int(i) for i in items.split()]
    return (ranges, items)

def is_contained(small, big):
    return small[0] >= big[0] and small[1] <= big[1]

def is_touching(r1,r2):
    return (r1[0] <= r2[0] <= r1[1]) or (r2[0] <= r1[0] <= r2[1])

# assume touching
def add_ranges(r1,r2):
    all_points = r1 + r2
    return [min(all_points), max(all_points)]

def range_size(r):
    return r[1] - r[0] + 1

def part1(parsed):
    fresh = []
    ranges, items = parsed
    for i in items: 
        spoiled = True
        for range in ranges:
            if range[0] <= i <= range[1]:
                spoiled = False
                break
        if not spoiled:
            fresh.append(i)
    return len(fresh)

def part2(parsed):
    ranges, _ = parsed
    ranges.sort()
    ret = [ranges.pop()]
    while len(ranges) != 0:
        r = ret.pop()
        r1 = ranges.pop()
        if not is_touching(r, r1):
            ret.append(r)
            ret.append(r1)
        else:
            if is_contained(r, r1):
                ret.append(r1)
            elif is_contained(r1, r):
                ret.append(r)
            else:
                ret.append(add_ranges(r, r1))
    return sum([range_size(r) for r in ret])

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
