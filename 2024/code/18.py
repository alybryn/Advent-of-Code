DAY = 18

START = f'/workspaces/Advent of Code/2024'
SAMPLE_PATH = f'{START}/sample/{DAY}.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]

RUN = ONLY_DATA

# --------------------------------

from collections import deque
import pathlib
import sys

SAMPLE_ANSWER_1 = 22
SAMPLE_ANSWER_2 = 6,1

PROBLEM_SPACE, SLICE = ((6,6),12) if RUN == ONLY_SAMPLE else ((70,70),1028)

def parse(puzzle_input):
    # parse the input
    lines = [line.split(',') for line in puzzle_input.splitlines()]
    ret = []
    for line in lines:
        i,j = line
        ret.append((int(i),int(j)))
    return ret
    
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
    return path

def draw_it(walls, path):
    ret = ''
    for j in range(0,PROBLEM_SPACE[1]+1):
        for i in range(0,PROBLEM_SPACE[0]+1):
            if (i,j) in walls:
                ret += '#'
                if (i,j) in path:
                    print('path in corruption')
            elif (i,j) in path:
                ret += 'O'
            elif (i,j) == (0,0):
                ret += 'S'
            else:
                ret += '.'
        ret += '\n'
    return ret

def part1(parsed):
    walls = set(parsed[:SLICE])
    start = (0,0)
    end = PROBLEM_SPACE
    graph = bfs(walls, start,end)
    path = count_path(graph, start, end)
    return len(path)

def part2(parsed):
    bytes_falling = parsed
    start = (0,0)
    end = PROBLEM_SPACE
    for i in range(SLICE,len(bytes_falling)):
        graph = bfs(set(bytes_falling[:i]),start, end)
        path = count_path(graph,start,end)
        if not path:
            return bytes_falling[i-1]

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