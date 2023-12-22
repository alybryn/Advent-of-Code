from collections import namedtuple
from enum import Enum
import pathlib
import sys

SAMPLE_ANSWER_1 = 5
SAMPLE_ANSWER_2 = 7

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
        self._supporting = set()
        self._supporters = set()

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

    def add_supporting(self, brick):
        self._supporting.add(brick)

    def add_supporters(self,brick):
        self._supporters.add(brick)

    @property
    def single_support(self):
        return len(self._supporters) == 1
    
    def all_support_removed(self, removed_bricks):
        for supporter in self._supporters:
            if supporter not in removed_bricks:
                return False
        return True

    @property
    def removable(self):
        for neighbor in self._supporting:
            if neighbor.single_support:
                return False
        return True
    
    @property
    def supporting(self):
        return self._supporting

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
    
    def up_neighbors(self):
        ret = []
        match self._orientation:
            case Orientation.X:
                for x in self.range:
                    ret.append(Point_3D(x,self._point1.y,self._point1.z+1))
            case Orientation.Y:
                for y in self.range:
                    ret.append(Point_3D(self._point1.x,y,self._point1.z+1))
            case Orientation.Z:
                ret.append(Point_3D(self._point1.x,self._point1.y,max(self._point1.z,self._point2.z)+1))
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

    # doubly links all bricks with the bricks resting on them
    def support_map(self):
        for z in self._bricks.keys():
            for brick in self._bricks[z]:
                for neighbor in brick.up_neighbors():
                    if neighbor in self._occupied:
                        neighbor_brick = self.brick_lookup(neighbor)
                        brick.add_supporting(neighbor_brick)
                        neighbor_brick.add_supporters(brick)

    # method for finding a brick resting on another brick (bricks are indexed by LOWEST z)
    def brick_lookup(self,point):
        for brick in self._bricks.get(point.z):
            if point in brick.all_points:
                return brick
    
    def find_removable(self):
        ret = 0
        for z in self._bricks.keys():
            for brick in self._bricks[z]:
                if brick.removable:
                    ret += 1
        return ret
    
    def find_chain(self):
        ret = 0
        for z in self._bricks.keys():
            for brick in self._bricks[z]:
                falling = set()
                now_falling = {brick}
                while len(now_falling) != len(falling):
                    falling.update(now_falling)
                    for brick in falling:
                        for supported in brick.supporting:
                            if supported.all_support_removed(falling):
                                now_falling.add(supported)
                ret += len(falling)-1
        return ret

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
    return settle_on_down(ret)

def settle_on_down(snap_shot):
    settled = Brick_Stack()
    for z in sorted(snap_shot.keys()):
        for brick in snap_shot.get(z):
            settled.set(brick)
    return settled

def part1(parsed):
    brick_stack = parsed
    brick_stack.support_map()

    return brick_stack.find_removable()

def part2(parsed):
    return parsed.find_chain()

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