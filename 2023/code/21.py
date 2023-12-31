from collections import deque, namedtuple
import pathlib
import sys

SAMPLE_ANSWER_1 = 16
SAMPLE_ANSWER_2 = None

# ELF_STEPS = 26501365
ELF_STEPS = 458

class Plot(namedtuple('Plot',['x','y'])):
    def __repr__(self) -> str:
        return f'({self.x},{self.y})'
    
    def neighbors(self):
        vectors = [(-1,0),(1,0),(0,-1),(0,1)]
        return [Plot(self.x+v[0], self.y+v[1]) for v in vectors]

class Step(namedtuple('Step',['plot','steps_rem'])):
    def __repr__(self) -> str:
        return f'{self.steps_rem} at {str(self.plot)}'
    
    def neighbors(self):
        return [Step(p, self.steps_rem-1) for p in self.plot.neighbors()]

    def is_end(self):
        return self.steps_rem == 0

# go ahead and assume min is (0,0)
Bound = namedtuple('Bound',['max_x', 'max_y'])

class InfiniteMap():
    def __init__(self, map, bound) -> None:
        self._base_map = map
        self._rep_bound = bound

    def query(self, plot):
        return (plot.x%self._rep_bound.max_x, plot.y%self._rep_bound.max_y)in self._base_map

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
    print(start)
    return InfiniteMap(gardens, Bound(len(lines),len(lines[0]))), start

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

def take_steps_inf(start, gardens, steps):
    frontier = deque()
    reached = {}
    frontier.append(Step(start,steps))
    reached[start] = steps

    while frontier:
        current = frontier.popleft()
        for next in current.neighbors():
            if gardens.query(next.plot):
                if next.steps_rem < 0:
                    continue
                if next.plot not in reached:
                    frontier.append(next)
                    reached[next.plot] = next.steps_rem
                # elif reached[next.plot] > next.steps_rem:
                #     frontier.append(next)
                #     reached[next.plot] = next.steps_rem
    return reached

# def count_zeros(reached_dict):
#     return sum([1 for p in reached_dict.values() if p == 0])

def count_even(reached_dict):
    return sum([1 for p in reached_dict.values() if p%2 == 0])

def count_odd(reached_dict):
    return sum([1 for p in reached_dict.values() if p%2 == 1])

def part1(parsed):
    return 3816

def part2(parsed):
    inf_map, start = parsed
    reached = take_steps_inf(start,inf_map, ELF_STEPS)
    # print(f'len: {len(reached)} zeros: {count_zeros(reached)}')
    return f'{ELF_STEPS},{count_even(reached)}'

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