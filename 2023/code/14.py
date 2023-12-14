from copy import deepcopy
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
 
class Platform():
    def __init__(self, input) -> None:
        self._bounds = {Direction.NORTH:0,
                        Direction.SOUTH:len(input),
                        Direction.EAST:len(input[0]),
                        Direction.WEST:0
                        }
        self._map = {}
        for x in range(self._bounds.get(Direction.SOUTH)):
            for y in range(self._bounds.get(Direction.EAST)):
                if input[x][y] != '.':
                    # round is True, square is False, none is None
                    self._map.update({(x,y): input[x][y] == 'O'})

    def inside(self, loc):
        return self._bounds.get(Direction.NORTH) <= loc[0] < self._bounds.get(Direction.SOUTH) and self._bounds.get(Direction.WEST) <= loc[1] < self._bounds.get(Direction.EAST)

    def spin(self, cycles):
        for i in range(cycles):
            # print('north')
            self.tilt_north()
            # print(self)
            # print('west')
            self.tilt_west()
            # print(self)
            # print('south')
            self.tilt_south()
            # print(self)
            # print('east')
            self.tilt_east()
            # print(self)

    def tilt_north(self):
        for x in range(self._bounds.get(Direction.SOUTH)):
            for y in range(self._bounds.get(Direction.EAST)):
                self.tilt(Direction.NORTH, x, y)

    def tilt_west(self):
        for x in range(self._bounds.get(Direction.SOUTH)):
            for y in range(self._bounds.get(Direction.EAST)):
                self.tilt(Direction.WEST, x, y)

    def tilt_south(self):
        for x in reversed(range(self._bounds.get(Direction.SOUTH))):
            for y in range(self._bounds.get(Direction.EAST)):
                self.tilt(Direction.SOUTH, x, y)

    def tilt_east(self):
        for x in range(self._bounds.get(Direction.SOUTH)):
            for y in reversed(range(self._bounds.get(Direction.EAST))):
                self.tilt(Direction.EAST, x, y)

    def tilt(self, direction, x, y):
        k = (x,y)
        rock = self._map.get(k)
        # print(f'{k}: {rock}')
        if rock:
            new = self.tilt_at(direction, k)
            if new != k:
                self._map.update({new: rock})
                self._map.update({k: None})
            # print(f'moved rock from {k} to {new}')

    # args are Direction and location of a round rock
    ### ONLY TILT TO ZERO! AND MAX ###
    def tilt_at(self, direction, loc):
        next_loc = neighbor(loc, direction)
        # print(f'rock at {next_loc} is {self._map.get(next_loc)}')
        while self.inside(next_loc) and self._map.get(next_loc) == None:
            loc = next_loc
            next_loc = neighbor(loc, direction)

        return loc

    def north_load(self):
        ret = 0
        for k in self._map.keys():
            if self._map.get(k):
                ret += self._bounds.get(Direction.SOUTH) - k[0]
        return ret

    def __str__(self) -> str:
        p = 'Platform:\n'
        for x in range(self._bounds.get(Direction.SOUTH)):
            for y in range(self._bounds.get(Direction.EAST)):
                r = self._map.get((x, y))
                p += 'O' if r else '.' if r == None else '#'
            p += '\n'
        return p

def part1(parsed):
    # print(parsed)
    this_platform = deepcopy(parsed)
    this_platform.tilt_north()
    # print(parsed)
    return this_platform.north_load()

def part2(parsed):
    parsed.spin(1_000_000_000)
    return parsed.north_load()

def part2(parsed):
    return 0

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