DAY = 20

START = f'/workspaces/Advent of Code/2024'
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
"""There are 14 cheats that save 2 picoseconds.
There are 14 : 4 picoseconds.
There are 2 : 6 picoseconds.
There are 4 : 8 picoseconds.
There are 2 : 10 picoseconds.
There are 3  12 picoseconds.
There is one : 20 picoseconds.
There is one : 36 picoseconds.
There is one : 38 picoseconds.
There is one : 40 picoseconds.
There is one : 64 picoseconds."""
SAMPLE_ANSWER_2 = None

BOUNDS = None

def parse(puzzle_input):
    # parse the input
    puzzle_input = [[l for l in line] for line in puzzle_input.splitlines()]
    global BOUNDS
    BOUNDS = (len(puzzle_input[0]), len(puzzle_input))
    track = set()
    start = None
    end = None
    for j in range(0,BOUNDS[0]):
        for i in range(0,BOUNDS[1]):
            if puzzle_input[j][i] == 'S':
                start = (i,j)
            elif puzzle_input[j][i] == 'E':
                end = (i,j)
            elif puzzle_input[j][i] == '.':
                track.add((i,j))
    track.add(start)
    track.add(end)
    # print(draw_it(track,start,end))
    steps = get_step_count(track, start, end)
    return steps

def get_step_count(track, start, end):
    ret = {}
    curr = start
    ret[start] = 0
    while curr != end:
        for neighbor in neighbors(current):
            if neighbor not in ret and neighbor in track:
                ret[neighbor] = ret[curr] + 1
    return ret

def neighbors(loc, cheating=False):
    step = 2 if cheating else 1
    # minus = -2 if cheating else -1

def draw_it(track,start=None,end=None):
    ret = ''
    for j in range(0,BOUNDS[1]):
        for i in range(0,BOUNDS[1]):
            if (i,j) == start:
                ret += 'S'
            elif (i,j) == end:
                ret += 'E'
            elif (i,j) in track:
                ret += '.'
            else:
                ret += '#'
        ret += '\n'
    return ret

def part1(parsed):
    print(parsed)
    time_saving_goal = 4
    c = 0
    for track in parsed.keys():
        for neighbor in neighbors(track, cheating=True):
            if neighbor in parsed:
                if parsed[neighbor] - parsed[track] >= time_saving_goal:
                    c +=1
    return c

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
