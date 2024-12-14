DAY = 14

START = f'/home/abi/Documents/programming/Advent of Code/2024'
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
    lines = puzzle_input.splitlines()
    for line in lines:
        _, p, v = line.split('=')
        p, _ = p.split (' ')
        px, py = p.split(',')
        vx, vy = v.split(',')

class Robot():
    def __init__(self,px,py,vx,vy):
        self._px = px
        self._py = py
        self._vx = vx
        self._vy = vy

    def where(self,bounds,time):
        return ((self._px+(self._vx*time))%bounds[0],
        (self._py+(self._vy*time)%bounds[1]))

def quardrant_count(robot, bounds, time):
    loc = robot.where(bounds, time)
    print(loc)
    if loc[0] < bounds[0]//2:
        if loc[1]< bounds[1]//2:
            return 'nw'
        # Todo
    # todo

def part1(parsed):
    bounds = (11,7) if RUN == ONLY_SAMPLE else (101,103)
    time = 100
    print(parsed)
    ret = {'nw':0,'ne':0,'sw':0,'se':0}
    for robot in parsed:
        q = quardrant_count(robot, bounds, time)
        if q in ret:
            ret[q] += 1
    return ret

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