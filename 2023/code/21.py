from collections import deque, namedtuple
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
    
    def reduce(self, bound):
        new_x = self.x
        new_y = self.y
        while new_x >= bound.max_x:
            new_x = new_x - bound.max_x
        while new_x < 0:
            new_x = new_x + bound.max_x
        while new_y >= bound.max_y:
            new_y = new_y - bound.max_y
        while new_y < 0:
            new_y = new_y + bound.max_y
        return Plot(new_x,new_y)

class Step(namedtuple('Step',['plot','steps_rem'])):
    def __repr__(self) -> str:
        return f'{self.steps_rem} at {str(self.plot)}'
    
    def neighbors(self):
        return [Step(p, self.steps_rem-1) for p in self.plot.neighbors()]

    def is_end(self):
        return self.steps_rem == 0

# go ahead and assume min is (0,0)
Bound = namedtuple('Bound',['max_x', 'max_y'])
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
                gardens.add(Plot(x,y))
                start = Plot(x,y)
    return gardens, start

def take_steps(start, gardens, steps):
    frontier = deque()
    reached = set()
    ends = set()
    frontier.append(Step(start,steps))
    reached.add(start)

    while frontier:
        current = frontier.popleft()
        for next in current.neighbors():
            if next.plot in gardens:
                if next.is_end():
                    ends.add(next.plot)
                elif next not in reached:
                    frontier.append(next)
                    reached.add(next)
    return ends

def part1(parsed):
    gardens, start = parsed
    ends = take_steps(start, gardens, 64)
    return len(ends)

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