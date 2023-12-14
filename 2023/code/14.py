from copy import copy
from functools import cache
import pathlib
from enum import Enum
import sys

SAMPLE_ANSWER_1 = 136
SAMPLE_ANSWER_2 = 64

def parse(puzzle_input):
    # parse the input
    lines = [list(line) for line in puzzle_input.split()]
    south_bound = len(lines)
    east_bound = len(lines[0])
    platform = {}
    switch = {'O': True, '#': False, '.': None}
    for x in range(south_bound):
        for y in range(east_bound):
            # round is True, square is False, none is None
            platform.update({(x,y): switch.get(lines[x][y])})

    return platform, south_bound, east_bound

class Direction(Enum):
    NORTH = (-1,0)
    WEST = (0,-1)
    SOUTH = (1, 0)
    EAST = (0,1)

@cache
def neighbor(loc, direction):
    return loc[0] + direction.value[0], loc[1] + direction.value[1]

def print_platform(platform, south_bound, east_bound):
    p = 'Platform:\n'
    for x in range(south_bound):
        for y in range(east_bound):
            r = platform.get((x, y))
            p += 'O' if r else '.' if r == None else '#'
        p += '\n'
    print(p)

def print_section(section):
    p = ''
    for v in section:
        p += 'O' if v else '.' if v == None else '#'
    print(p)

def north_load(platform, south_bound):
        ret = 0
        for k in platform.keys():
            if platform.get(k):
                ret += south_bound - k[0]
        return ret

def spin(platform, cycles, south_bound, east_bound):
    for _ in range(cycles):
        tilt_north(platform, south_bound, east_bound)
        tilt_west(platform, south_bound, east_bound)
        tilt_south(platform, south_bound, east_bound)
        tilt_east(platform, south_bound, east_bound)

    return platform

def tilt_north(platform, south_bound, east_bound):
    for y in range(east_bound):
        section = []
        for x in range(south_bound):
            section.append(platform.get((x, y)))
        section = fall_down(tuple(section))
        for x in range(east_bound):
            platform.update({(x,y): section[x]})

def tilt_west(platform, south_bound, east_bound):
    for x in range(south_bound):
        section = []
        for y in range(east_bound):
            section.append(platform.get((x,y)))
        section = fall_down(tuple(section))
        for y in range(east_bound):
            platform.update({(x,y): section[y]})

def tilt_south(platform, south_bound, east_bound):
    for y in range(east_bound):
        section = []
        for x in reversed(range(south_bound)):
            section.append(platform.get((x,y)))
        section = fall_down(tuple(section))
        for x in range(south_bound):
            platform.update({(x,y): section[south_bound-x-1]})

def tilt_east(platform, south_bound, east_bound):
    for x in range(south_bound):
        section = []
        for y in reversed(range(east_bound)):
            section.append(platform.get((x,y)))
        section = fall_down(tuple(section))
        for y in range(east_bound):
            platform.update({(x,y): section[east_bound-y-1]})

@cache
def fall_down(section):
    section = list(section)
    for i in range(len(section)):
        if section[i]:
            next_i = i
            while next_i - 1 >= 0 and section[next_i - 1] == None:
                next_i = next_i-1
            section[next_i] = True
            if i != next_i:
                section[i] = None
    return tuple(section)
 
def part1(parsed):
    platform = copy(parsed[0])
    south_bound = parsed[1]
    east_bound = parsed[2]
    tilt_north(platform, south_bound, east_bound)
    return north_load(platform, south_bound)

def part2(parsed):
    platform = copy(parsed[0])
    south_bound = parsed[1]
    east_bound = parsed[2]
    cycles = 1_000_000_000
    # cycles = 3
    spin(platform, cycles, south_bound, east_bound)
    return north_load(platform, south_bound)

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}")
        puzzle_input = pathlib.Path(path).read_text().strip()

        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))