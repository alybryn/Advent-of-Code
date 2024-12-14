DAY = 14

START = f'/workspaces/Advent of Code/2024'
SAMPLE_PATH = f'{START}/sample/{DAY}.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]
ALL = [SAMPLE_PATH, DATA_PATH]

RUN = ONLY_DATA

# --------------------------------

import pathlib
import sys

SAMPLE_ANSWER_1 = 12
SAMPLE_ANSWER_2 = None

BOUNDS = (11,7) if RUN == ONLY_SAMPLE else (101,103)

def parse(puzzle_input):
    # parse the input
    lines = puzzle_input.splitlines()
    robots = []
    for line in lines:
        _, p, v = line.split('=')
        p, _ = p.split (' ')
        px, py = p.split(',')
        vx, vy = v.split(',')
        inputs = [int(i) for i in [px,py,vx,vy]]
        robots.append(Robot(*inputs))
    return robots

class Robot():
    def __init__(self,px,py,vx,vy):
        self._px = px
        self._py = py
        self._vx = vx
        self._vy = vy

    def where(self,time):
        return (((self._px+(self._vx*time)))%BOUNDS[0],
        ((self._py+(self._vy*time))%BOUNDS[1]))
    
    def __repr__(self):
        return f'ROBOT[p={self._px},{self._py} v={self._vx},{self._vy}]'

def quadrant_count(robot, time):
    loc = robot.where(time)
    half_bounds = (BOUNDS[0]//2,BOUNDS[1]//2)
    east_west = loc[0] < half_bounds[0],loc[0] > half_bounds[0]
    north_south = loc[1] < half_bounds[1],loc[1] > half_bounds[1]
    if north_south[0] and east_west[0]:
        return 'nw'
    if north_south[0] and east_west[1]:
        return 'ne'
    if north_south[1] and east_west[0]:
        return 'sw'
    if north_south[1] and east_west[1]:
        return 'se'

def part1(parsed):
    time = 100
    # print(parsed)
    ret = {'nw':0,'ne':0,'sw':0,'se':0}
    for robot in parsed:
        q = quadrant_count(robot, time)
        if q in ret:
            ret[q] += 1
    safety = 1
    for c in ret.values():
        safety = safety * c
    return safety

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