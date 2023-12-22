from collections import namedtuple
from enum import Enum
import pathlib
import sys

SAMPLE_ANSWER_1 = 5
SAMPLE_ANSWER_2 = None

Point_3D = namedtuple('Point_3D', ['x','y','z'])

class Orientation(int,Enum):
    X = 0
    Y = 1
    Z = 2

class SandBrick():
    def __init__(self,coords) -> None:
        self._point1 = Point_3D(coords[0][0],coords[0][1],coords[0][2])
        self._point2 = Point_3D(coords[1][0],coords[1][1],coords[1][2])
        self._orientation = Orientation.X if self._point1.x != self._point2.x else Orientation.Y if self._point1.y != self._point2.y else Orientation.Z

    @property
    def lowest(self):
        return min(self._point1.z,self._point2.z)
    
    
    def __repr__(self) -> str:
        return f'{self._point1.x},{self._point1.y},{self._point1.z}~{self._point2.x},{self._point2.y},{self._point2.z}'

def parse(puzzle_input):
    # parse the input
    lines = puzzle_input.split()
    # dictionary of bricks with lowest point z {z:[SandBrick]}
    ret = {}
    for line in lines:
        brick = SandBrick([[int(i) for i in part.split(',')] for part in line.split('~')])
        level = ret.get(brick.lowest,[])
        level.append(brick)
        ret[brick.lowest]=level
    return ret

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