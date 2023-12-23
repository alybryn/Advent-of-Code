from collections import namedtuple
import pathlib
import sys

SAMPLE_ANSWER_1 = 94
SAMPLE_ANSWER_2 = None

class Path(namedtuple('Path',['x','y','slope'])):
    def __repr__(self):
        return f'{self.x},{self.y}:{self.slope}'

    def neighbors(self):
        pass

def parse(puzzle_input):
    # parse the input
    lines =  puzzle_input.split()
    start = None
    end = None
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if x == 0 and lines[x][y]=='.':
                start = Path(x,y,lines[x][y])
            if x == len(lines)-1 and lines[x][y]=='.':
                end = Path(x,y,lines[x][y])
            Path(x,y,lines[x][y])

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
