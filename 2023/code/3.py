import pathlib
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    lines = puzzle_input.split()
    # length = len(lines)
    width = len(lines[0])
    points = {}
    nums = []
    for i in range(len(lines)):
        j = 0
        while j < width:
            if lines[i][j].isdigit():
                # start getting number
                n = ''
                p = []
                while lines[i][j].isdigit():
                    n += lines[i][j]
                    p.append((i, j))
                    # overwriting numbers for now
                    points.update({(i, j): '.'})
                    j += 1
            else:
                points.update({(i, j): lines[i][j]})
                j += 1
        p +='\n'
    return (points, nums)


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
    
    @property
    def value(self):
        return self._value

def part1(parsed):
    print(parsed)
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