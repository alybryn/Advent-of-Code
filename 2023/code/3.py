import pathlib
import sys

SAMPLE_ANSWER_1 = 4361
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    lines = puzzle_input.split()
    # print(lines)
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
                    if j == width:
                        break
                # acutally create and save Nums
                nums.append(Num(int(n),p))
            else:
                points.update({(i, j): lines[i][j]})
                j += 1
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
    def neighbors(self):
        ret = set()
        # diagonals too
        matrix = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (1,1), (-1,1), (1,-1)]

        # add neighbors for each point
        for p in self._points:
            for m in matrix:
                a = (p[0] + m[0], p[1] + m[1])
                # prevention is the best cure:
                if a not in self._points:
                    ret.add(a)
        return ret
    
    @property
    def value(self):
        return self._value

def part1(parsed):
    # add part numbers
    ret = 0
    mapping = parsed[0]
    numbers = parsed[1]
    for n in numbers:
        # part numbers are adjacent to non '.' chars
        for p in n.neighbors:
            if mapping.get(p, '.') != '.':
                ret += n.value
                break
    return ret

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