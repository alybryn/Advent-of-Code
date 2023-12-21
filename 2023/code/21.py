from collections import namedtuple
import pathlib
import sys

SAMPLE_ANSWER_1 = 16
SAMPLE_ANSWER_2 = None

class Plot(namedtuple('Plot',['x','y'])):
    def __repr__(self) -> str:
        return f'({self.x},{self.y})'
    
    def neighbors(self):
        vectors = [(-1,0),(1,0),(0,-1),(0,1)]
        return [Plot(self.x+v[0], self.y+v[1]) for v in vectors]

def parse(puzzle_input):
    # parse the input
    gardens = set()
    start = None
    lines = puzzle_input.split()
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if lines[x][y] == '.':
                gardens.add(Plot(x,y))
            elif lines[x][y] == 'S':
                start = Plot(x,y)
    return gardens, start

def part1(parsed):
    gardens, start = parsed
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