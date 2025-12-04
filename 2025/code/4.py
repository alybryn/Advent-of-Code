DAY = 4
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

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return [[c for c in list(s)] for s in puzzle_input.split()]

def adj(i, j):
    mod = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
    return [(i + m[0],j + m[1]) for m in mod]

def remove_paper(map):
    ret = ''
    bounds = (len(map),len(map[0]))
    for i in range(0, bounds[0]):
        for j in range(0, bounds[1]):
            if map[i][j] == '@':
                adjacent_rolls = 0
                for a  in adj(i, j):
                    if 0 <= a[0] < bounds[0] and 0 <= a[1] < bounds[1]:
                        if map[a[0]][a[1]] == '@': adjacent_rolls += 1
                if adjacent_rolls < 4:
                    ret += '.'
                else:
                    ret += '@'
            else:
                ret += '.'
        ret += '\n'
    return ret

def count_rolls(map):
    return sum([sum([1 for x in y if x == '@']) for y in map])

def part1(parsed):
    return count_rolls(parsed) - count_rolls(remove_paper(parsed))

def part2(parsed):
    prev = parsed
    curr = remove_paper(prev)
    ret = count_rolls(prev) - count_rolls(curr)
    while prev != curr:
        prev = curr
        curr = remove_paper(prev)
        ret += count_rolls(prev) - count_rolls(curr)
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
