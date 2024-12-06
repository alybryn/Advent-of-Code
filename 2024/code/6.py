from enum import Enum
import pathlib
import sys

SAMPLE_ANSWER_1 = 41
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    lines = [[l for l in line] for line in puzzle_input.split('\n')]
    obstacles = set()
    guard = None
    upper_bounds = (len(lines)-1,len(lines[0])-1)
    for i in range(0, len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "#":
                obstacles.add((i,j))
            elif lines[i][j] == "^":
                guard = Guard((i,j))
    return guard, obstacles, upper_bounds

class Direction(Enum):
    N = (-1, 0)
    S = ( 1, 0)
    E = ( 0, 1)
    W = ( 0,-1)

    NINTY = {N:E,
             E:S,
             S:W,
             W:N,
             }

class Guard():
    def __init__(self, loc):
        self.dir = Direction.N
        self.loc = loc

    def in_bounds(self, uppers):
        return 0 < self.loc[0] < uppers[0] and 0 <= self.loc[1] <= uppers[1]
    
    def forward(self):
        pass

def part1(parsed):
    print(parsed)
    guard, obstacles, upper_bounds = parsed
    occupied = {guard.loc}
    while guard.in_bounds(upper_bounds):
        guard.forward()
    return occupied

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
