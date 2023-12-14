from functools import cache
import pathlib
from enum import Enum
import sys

SAMPLE_ANSWER_1 = 136
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return Platform([list(line) for line in puzzle_input.split()])

class Direction(Enum):
    NORTH = (-1,0)
    SOUTH = (1, 0)
    EAST = (0,1)
    WEST = (0,-1)

@cache
def neighbor(loc, direction):
    return loc[0] + direction.value[0], loc[1] + direction.value[1]
 
class Platform():
    def __init__(self, input) -> None:
        self._bounds = {Direction.NORTH:0,
                        Direction.SOUTH:len(input),
                        Direction.EAST:len(input[0]),
                        Direction.WEST:0
                        }
        self._map = {}
        for x in range(self._southern_edge):
            for y in range(self._eastern_edge):
                if input[x][y] != '.':
                    # round is True, square is False, none is None
                    self._map.update({(x,y): input[x][y] == 'O'})

    def tilt(self, direction):
        for x in range(self._bounds.get(Direction.SOUTH)):
            for y in range(self._bounds.get(Direction.EAST)):
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
        while next_loc[0] >= 0 and self._map.get(next_loc) == None:
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
    parsed.tilt(Direction.NORTH)
    # print(parsed)
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