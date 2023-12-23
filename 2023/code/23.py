from collections import deque, namedtuple
import pathlib
import sys

SAMPLE_ANSWER_1 = 94
SAMPLE_ANSWER_2 = None

class Path(namedtuple('Path',['x','y'])):
    def __repr__(self):
        return f'({self.x},{self.y})'

    def neighbors(self,slope):
        switch = {'.':[(-1,0),(1,0),(0,-1),(0,1)],
                  '^':[(-1,0)],
                  'v':[(1,0)],
                  '>':[(0,1)],
                  '<':[(0,-1)]}
        matrix = switch[slope]
        return [Path(self.x+m[0], self.y+m[1]) for m in matrix]

def parse(puzzle_input):
    # parse the input
    lines =  puzzle_input.split()
    paths = {}
    start = lines[0]
    end = lines[-1]
    lines = lines[1:-1]

    for y in range(len(lines[0])):
        if start[y] == '.':
            start_path = Path(0,y)
            paths['start'] = start_path
            paths[start_path] = '.'
        if end[y] == '.':
             end_path = Path(len(lines)-1,y)
             paths['end'] = end_path
             paths[end_path] = '.'
        for x in range(len(lines)):
            if lines[x][y] == '#':
                continue
            paths[Path(x,y)] = lines[x][y]
    
    return paths

def weigh(path):
    start = path['start']
    frontier = deque()
    frontier.append(start)
    reached = set()
    reached.add(start)
    weights = {}
    while frontier:
        current = frontier.popleft()
        for next in current.neighbors(path[current]):
            if next in path:
                if next not in reached:
                    frontier.append(next)
                    reached.add(next)

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
