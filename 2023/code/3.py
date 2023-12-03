import pathlib
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return [line for line in puzzle_input.split()]

# def xy_neighbors(pair):
#     # diagonals too
#     matrix = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (1,1), (-1,1), (1,-1)]
#     return [(pair[0] + m[0], pair[1] + m[1]) for m in matrix]

class Num():
    # val: int, points: [(x,y),...]
    def __init__(self, value, points):
        self._value = value
        self._points = points
    
    @property
    def neigbors(self):
        ret = set()
        # diagonals too
        matrix = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (1,1), (-1,1), (1,-1)]
        for p in self._points:
            ret.add([(p[0] + m[0], p[1] + m[1]) for m in matrix])
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