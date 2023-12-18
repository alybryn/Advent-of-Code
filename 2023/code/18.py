from collections import namedtuple, deque
import pathlib
import sys

SAMPLE_ANSWER_1 = 62
SAMPLE_ANSWER_2 = 952408144115

NEIGHBORS = [(-1, 0), ( 1, 0), ( 0, 1), ( 0,-1)]

# DIRECTIONS = {'U':(-1, 0),'D':( 1, 0),'R':( 0, 1), 'L':( 0,-1)}
DIRECTIONS = {
    'U': lambda x,y,d: Point(x-d,y),
    'D': lambda x,y,d: Point(x+d,y),
    'L': lambda x,y,d: Point(x,y-d),
    'R': lambda x,y,d: Point(x,y+d),
     3 : lambda x,y,d: Point(x-d,y),
     1 : lambda x,y,d: Point(x+d,y),
     2 : lambda x,y,d: Point(x,y-d),
     0 : lambda x,y,d: Point(x,y+d),
    }
NUMBER_DIRECTIONS = {
     0 : DIRECTIONS['R'],
     1 : DIRECTIONS['D'],
     2 : DIRECTIONS['L'],
     3 : DIRECTIONS['U'],
}

class Point(namedtuple('Point', ['x','y'])):
    def __repr__(self) -> str:
        return f'({self.x},{self.y})'
    
    def add(self, other):
        return Point(self.x + other[0], self.y + other[1])
    
    def neighbors(self):
        return [self.add(vector) for vector in NEIGHBORS]

class Line(namedtuple('Line', ['p1','p2'])):
    def __repr__(self) -> str:
        return f'{self.p1}->{self.p2}'

    @property
    def len(self):
        return abs(self.p1.x-self.p2.x) + abs(self.p1.y-self.p2.y)

class Bound(namedtuple('Bound', ['min','max'])):
    def __repr__(self) -> str:
        return f'Within {self.min}, {self.max}'
    
    def contains(self, point):
        return self.min.x <= point.x <= self.max.x and self.min.y <= point.y <= self.max.y
    
    def expand_to_include(self,point):
        return Bound(Point(min(self.min.x,point.x),min(self.min.y,point.y)), Point(max(self.max.x,point.x),max(self.max.y,point.y)))

class Graph():
    def __init__(self) -> None:
        self._lines = []
    
    def add(self, p1, p2):
        self._lines.append(Line(p1,p2))

    def volume(self):
        s = 0
        for line in self._lines:
            s += (line.p1.x*line.p2.y)-(line.p1.y*line.p2.x)
        return abs(s//2)

    @property
    def len(self):
        ret = 0
        for line in self._lines:
            ret += line.len
        return ret
    
    def __repr__(self) -> str:
        p = ''
        for line in self._lines:
            p += line.__repr__()
        return p

def parse(puzzle_input):
    small_lavaduct = Graph()
    small_curr = Point(0,0)

    big_lavaduct = Graph()
    big_curr = Point(0,0)
    
    lines = puzzle_input.split('\n')
    for line in lines:
        # Small lavaduct
        small_dir, small_dist, color = line.split(' ')
        small_dist = int(small_dist)

        new_point = DIRECTIONS[small_dir](small_curr.x,small_curr.y,small_dist)
        small_lavaduct.add(small_curr, new_point)
        small_curr = new_point

        # large lavaduct
        big_dist = int(color[2:-2],16)
        big_dir = int(color[-2:-1])

        new_point = NUMBER_DIRECTIONS[big_dir](big_curr.x,big_curr.y,big_dist)
        big_lavaduct.add(big_curr, new_point)
        big_curr = new_point

    return small_lavaduct, big_lavaduct

def part1(parsed):
    graph, _ = parsed
    return graph.volume() + (graph.len//2) + 1

def part2(parsed):
    _,graph = parsed
    return graph.volume() + (graph.len//2) + 1

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