from collections import namedtuple
from math import gcd, sqrt
import numpy as np
import pathlib
import sys

SAMPLE_ANSWER_1 = 2
SAMPLE_ANSWER_2 = None

SAMPLE_BOUND = (7,27)
DATA_BOUND = (200000000000000,400000000000000)

class Point3D(namedtuple('Point3D',['x','y','z'])):
    def __repr__(self) -> str:
        return f'({self.x},{self.y},{self.z})'

    def add(self,vector):
        return Point3D(self.x+vector.a,self.y+vector.b,self.z+vector.c)
    
class Vector3D(namedtuple('Vector3D',['a','b','c'])):
    def __repr__(self) -> str:
        return f'({self.a},{self.b},{self.c})'
    
    def is_parallel(self,other):
        return self.reduce() == other.reduce()
    
    def is_xy_parallel(self,other):
        s_r = self.reduce()
        o_r = other.reduce()
        return s_r.a == o_r.a and s_r.b == o_r.b

    def reduce(self):
        div = gcd(self.a,self.b,self.c)
        return Vector3D(self.a//div, self.b//div, self.c//div)

class Line3D(namedtuple('Line3D',['point','vector'])):
    def __repr__(self) -> str:
        return f'{str(self.point)} @ {str(self.vector)}'
    
    def is_parallel(self,other):
        return self.vector.is_parallel(other.vector)
    
    def is_xy_parallel(self,other):
        return self.vector.is_xy_parallel(other.vector)
    
    @property
    def other_point(self):
        return self.point.add(self.vector)
    
    @property
    def x(self):
        return self.point.x
    
    @property
    def y(self):
        return self.point.y
    
    @property
    def z(self):
        return self.point.z
    
    @property
    def a(self):
        return self.vector.a
    
    @property
    def b(self):
        return self.vector.b
    
    @property
    def c(self):
        return self.vector.c
        
def parse(puzzle_input):
    # parse the input
    ret = []
    for line in puzzle_input.split('\n'):
        pos, vec = line.split(' @ ')
        x,y,z = [int(p) for p in pos.split(', ')]
        a,b,c = [int(v) for v in vec.split(', ')]
        vec = Vector3D(a,b,c)
        pos = Point3D(x,y,z)
        ret.append(Line3D(pos,vec))
    return ret

# returns the position at which the lines intersect
def intersect_2D(line_a,line_b):
    A = np.array([[line_a.a,line_a.b],
                  [line_b.a,line_b.b]])
    
    b1 = (line_a.x*line_a.other_point.y - line_a.other_point.x*line_a.y)
    b2 = (line_b.x*line_b.other_point.y - line_b.other_point.x*line_b.y)
    b = -np.array([b1,b2])
    intersection_point = None
    try:
        intersection_point = np.linalg.solve(A,b)
    except np.linalg.LinAlgError:
        print("No single intersection point detected")
    return intersection_point

def part1(parsed):
    print(type(parsed))
    # for pair of lines, considering only their xy coordinates:
    # do they intersect
    c = 0
    for i in range(len(parsed)-1):
        for j in range(i+1,len(parsed)):
            print(f'A: {parsed[i]}\nB: {parsed[j]}')
            if parsed[i].is_xy_parallel(parsed[j]):
                print("lines do not intersect because parallel")
                if not parsed[i].is_parallel(parsed[j]):
                    print("xy parallel but not parallel")
            else:
                i = intersect_2D(parsed[i], parsed[j])
                if i.any():
                    print(i)
            c +=1
    return c

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