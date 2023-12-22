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
    
    @property
    def range(self):
        return range(self._range_min, self._range_max)
    
    @property
    def _range_min(self):
        if self._orientation == Orientation.X:
            return min(self._point1.x,self._point2.x)
        if self._orientation == Orientation.Y:
            return min(self._point1.y,self._point2.y)
        if self._orientation == Orientation.Z:
            return min(self._point1.z,self._point2.z)

    @property
    def _range_max(self):
        if self._orientation == Orientation.X:
            return max(self._point1.x,self._point2.x)+1
        if self._orientation == Orientation.Y:
            return max(self._point1.y,self._point2.y)+1
        if self._orientation == Orientation.Z:
            return max(self._point1.z,self._point2.z)+1

    def drop(self):
        self._point1 = Point_3D(self._point1.x,self._point1.y,self._point1.z-1)
        self._point2 = Point_3D(self._point2.x,self._point2.y,self._point2.z-1)

    @property
    def all_points(self):
        ret = set()
        match self._orientation:
            case Orientation.X:
                for x in self.range:
                    ret.add(Point_3D(x,self._point1.y,self._point1.z))
            case Orientation.Y:
                for y in self.range:
                    ret.add(Point_3D(self._point1.x,y,self._point1.z))
            case Orientation.Z:
                for z in self.range:
                    ret.add(Point_3D(self._point1.x,self._point1.y,z))
        return ret
    
    def down_neighbors(self):
        ret = []
        match self._orientation:
            case Orientation.X:
                for x in self.range:
                    ret.append(Point_3D(x,self._point1.y,self._point1.z-1))
            case Orientation.Y:
                for y in self.range:
                    ret.append(Point_3D(self._point1.x,y,self._point1.z-1))
            case Orientation.Z:
                ret.append(Point_3D(self._point1.x,self._point1.y,min(self._point1.z,self._point2.z)-1))
        return ret
    
    def __repr__(self) -> str:
        return f'{self._point1.x},{self._point1.y},{self._point1.z}~{self._point2.x},{self._point2.y},{self._point2.z}'
    
class Brick_Stack():
    def __init__(self) -> None:
        self._bricks = {}
        self._occupied = set()
    
    def set(self,brick):
        while brick.lowest > 1:
            for neighbor in brick.down_neighbors():
                if neighbor in self._occupied:
                    # done moving
                    self._occupied.update(brick.all_points)
                    level = self._bricks.get(brick.lowest,[])
                    level.append(brick)
                    self._bricks[brick.lowest] = level
                    return
            # move down:
            brick.drop()
        # settles on ground
        self._occupied.update(brick.all_points)
        level = self._bricks.get(brick.lowest,[])
        level.append(brick)
        self._bricks[brick.lowest] = level

    def __repr__(self) -> str:
        return str(self._bricks)

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

def settle_on_down(snap_shot):
    settled = Brick_Stack()
    for z in sorted(snap_shot.keys()):
        print(z)
        for brick in snap_shot.get(z):
            settled.set(brick)
    return settled

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