DAY = 18

START = f'/home/abi/Documents/programming/Advent of Code/2024'
SAMPLE_PATH = f'{START}/sample/{DAY}.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]

RUN = ONLY_SAMPLE

# --------------------------------

from collections import deque
import pathlib
import sys

SAMPLE_ANSWER_1 = 22
SAMPLE_ANSWER_2 = None

PROBLEM_SPACE = (6,6) if ONLY_SAMPLE else (70,70)

def parse(puzzle_input):
    # parse the input
    return set([(int(i),int(j)) for line in puzzle_input.splitlines()[:1024] for i,j in line.split(',')])

class Queue:
    def __init__(self):
        self._elements = deque()

    def empty(self): return not self._elements

    def put(self,x):
        self._elements.append(x)

    def get(self):
        return self._elements.popleft()

def bfs(corrupted, start, end):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()
        if current == end:
            break
        for next in neighbors(current):
            if next in corrupted:
                continue
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    
    return came_from

def neighbors(coord):
    x = lambda a: 0 <= a[0] <= PROBLEM_SPACE[0] and 0 <= a[1] <= PROBLEM_SPACE[1]
    return filter(x,[(coord[0]+i[0],coord[1]+i[1]) for i in [(-1,0),(1,0),(0,-1),(0,1)]])

def count_path(graph,start, end):
    if end not in graph: return set()
    current = end
    path = set()
    while current != start:
        path.add(current)
        current = graph[current]
    path.add(current)
    return path

def part1(parsed):
    print(parsed)
    path = bfs(parsed, (0,0),PROBLEM_SPACE)
    return len(path)

def part2(parsed):
    return 0

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

def run(path):
    print(f'{path}')
    puzzle_input = pathlib.Path(path).read_text().strip()

    solutions = solve(puzzle_input)
    print('\n'.join(str(solution) for solution in solutions))

if __name__ == "__main__":
    for path in RUN:
        run(path)
    for path in sys.argv[1:]:
        print('this program is not taking command line arguments.')