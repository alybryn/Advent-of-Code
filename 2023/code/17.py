from collections import namedtuple
from queue import PriorityQueue
import pathlib
import sys

SAMPLE_ANSWER_1 = 102
SAMPLE_ANSWER_2 = None

INF_COST = 1000000000000

def parse(puzzle_input):
    # parse the input
    ret = {}
    lines = [[int(l) for l in list(line)] for line in puzzle_input.split()]
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            ret.update({Block(x, y): lines[x][y]})
    return CityMap(ret, len(lines), len(lines[0]))

Bounds = namedtuple('Bounds', ['min_x', 'max_x', 'min_y', 'max_y'])

class Block(namedtuple('Block', ['x', 'y'])):
    def __repr__(self) -> str:
        return f'({self.x},{self.y})'

class CityMap():
    def __init__(self, blocks, max_x, max_y, min_y=0, min_x=0) -> None:
        self._heat_map = blocks
        self._dimensions = Bounds(min_x, max_x, min_y, max_y)
        self._edges = {}

        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                self._edges.update({Block(x, y):[Block(x  ,y-1),
                Block(x  ,y+1),
                Block(x-1,y  ),
                Block(x+1,y  )]})

    def neighbors(self, block):
        return self._edges.get(block)

    def cost(self, from_blocks, to_block):
        admissable = False
        for block in from_blocks:
            if block.x != to_block.x or block.y != to_block.y:
                admissable = True
        # this is where the ring of fire goes...
        return self._heat_map.get(to_block, INF_COST) if admissable else INF_COST
    
    def __str__(self) -> str:
        p = ''
        for x in range(self._dimensions.min_x, self._dimensions.max_x):
            for y in range(self._dimensions.min_y, self._dimensions.max_y):
                p += str(self._heat_map.get((x, y)))
            p += '\n'
        return p


def part1(parsed):
    return 0

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