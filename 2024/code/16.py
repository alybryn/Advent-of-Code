DAY = 16

START = f'/workspaces/Advent of Code/2024'
SAMPLE_PATH = f'{START}/sample/{DAY}.txt'
SAMPLE_PATH_A = f'{START}/sample/{DAY}a.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH_A, SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]
ALL = [SAMPLE_PATH, DATA_PATH]

RUN = ONLY_SAMPLE

# --------------------------------

import heapq
from enum import Enum
import pathlib
import sys

SAMPLE_ANSWER_1 = 7036, 11048
SAMPLE_ANSWER_2 = 45, 64

def parse(puzzle_input):
    # parse the input
    return set([(j,i) for i, line in enumerate(puzzle_input.splitlines()) for j,l in enumerate(line) if l == '#'])

class Direction(Enum):
    N = ( 0,-1)
    E = ( 1, 0)
    S = ( 0, 1)
    W = (-1, 0)

    def turn_left(self):
        return {
            Direction.N:Direction.W,
            Direction.W:Direction.S,
            Direction.S:Direction.E,
            Direction.E:Direction.N}[self]
    
    def turn_right(self):
        return {
            Direction.N:Direction.E,
            Direction.W:Direction.N,
            Direction.S:Direction.W,
            Direction.E:Direction.S}[self]
    
    def __lt__(self, other):
        return self.value < other.value
    
class PriorityQueue:
    def __init__(self):
        self._elements = []

    def empty(self): return not self._elements

    def put(self, x, cost): heapq.heappush(self._elements, (cost,x))

    def get(self): return heapq.heappop(self._elements)[1]

def dfs(walls, start, end):
    frontier = PriorityQueue()
    frontier.put(start,0)
    # dict[Loc, Optional[Loc]]
    came_from = {}
    # dict[Loc, float]
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        # only check loc, not dir
        if current[0] == end:
            return cost_so_far[current]

        for next,cost in neighbors(current):
            # check not in a wall
            if next[0] in walls:
                continue
            new_cost = cost_so_far[current] + cost
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                frontier.put(next,new_cost)
                came_from[next] = current
    
    return came_from, cost_so_far

# returns ((location, direction), cost)
def neighbors(loc_dir):
    loc,dir = loc_dir
    step_cost = 1
    turn_cost = 1000
    return [((coord_add(loc,dir.value),dir),step_cost),
            ((loc,dir.turn_left()),turn_cost),
            ((loc,dir.turn_right()),turn_cost)]

def coord_add(loc,vec): return (loc[0]+vec[0],loc[1]+vec[1])

def draw_race(walls, path=set()):
    bounds = max(walls)
    ret = ''
    for j in range(0,bounds[1]+1):
        for i in range(0,bounds[0]+1):
            if (i,j) in path: print('dingdong')
            ret += '#' if (i,j) in walls else '@' if (i,j) in path else '.'
        ret += '\n'
    return ret

def part1(parsed):
    # print(parsed)
    bounds = max(parsed)
    s = (1, bounds[1]-1)
    e = (bounds[0]-1, 1)
    cost = dfs(parsed,(s,Direction.E),e)
    return cost

def part2(parsed):
    # find ALL paths with min_cost
    # return len(set(path_coord)) (direction agnostic)
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
        run(path)