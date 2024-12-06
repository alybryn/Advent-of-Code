from enum import Enum
import pathlib
import sys

SAMPLE_ANSWER_1 = 41
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    lines = [[l for l in line] for line in puzzle_input.split('\n')]
    obstacles = set()
    upper_bounds = (len(lines)-1,len(lines[0])-1)
    guard = Guard((0,0),obstacles, upper_bounds)
    for i in range(0, len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "#":
                obstacles.add((i,j))
            elif lines[i][j] == "^":
                guard.set((i,j))
    return guard

class Direction(Enum):
    N = (-1, 0)
    S = ( 1, 0)
    E = ( 0, 1)
    W = ( 0,-1)
    
    def __repr__(self) -> str:
        return f"{self.name}"

class Guard():
    def __init__(self, loc, obstacles, bounds):
        self.dir = Direction.N
        self.loc = loc
        self.obstacles = obstacles
        self.bounds = bounds

    def set(self,loc):
        self.loc = loc

    def forward(self):
        step = self.__look_ahead__()
        if not step in self.obstacles:
            self.loc = step
            return True
        return False

    def turn(self):
        ninty = {Direction.N:Direction.E,
                 Direction.E:Direction.S,
                 Direction.S:Direction.W,
                 Direction.W:Direction.N
                 }
        self.dir = ninty.get(self.dir)

    def in_bounds(self):
        return 0 < self.loc[0] < self.bounds[0] and 0 < self.loc[1] < self.bounds[1]
    
    def __look_ahead__(self):
        return (self.loc[0] + self.dir.value[0],
                self.loc[1] + self.dir.value[1])

    def __isObstructed__(self,loc):
        return loc in self.obstacles

    def __repr__(self) -> str:
        return f"Guard at {self.loc} facing {self.dir}."

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
