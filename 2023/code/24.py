from collections import namedtuple
import pathlib
import sys

SAMPLE_ANSWER_1 = 2
SAMPLE_ANSWER_2 = None

SAMPLE_BOUND = (7,27)
DATA_BOUND = (200000000000000,400000000000000)

class Point3D(namedtuple('Point3D',['x','y','z'])):
    def __repr__(self) -> str:
        return f'({self.x},{self.y},{self.z})'

class Vector3D(namedtuple('Vector3D',['a','b','c'])):
    def __repr__(self) -> str:
        return f'({self.a},{self.b},{self.c})'

class Line3D(namedtuple('Line3D',['point','vector'])):
    def __repr__(self) -> str:
        return f'{str(self.point)} @ {str(self.vector)}'
        
def parse(puzzle_input):
    # parse the input
    ret = []
    for line in puzzle_input.split('\n'):
        pos, vec = line.split(' @ ')
        px,py,pz = pos.split(', ')
        vx,vy,vz = vec.split(', ')
        ret.append(Line3D(Point3D(px,py,pz),Vector3D(vx,vy,vz)))

    return ret

def part1(parsed):
    return parsed

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