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
    parsed = set([(j,i) for i, line in enumerate(puzzle_input.splitlines()) for j,l in enumerate(line) if l == '#'])
    bounds = max(parsed)
    start = (1, bounds[1]-1)
    end = (bounds[0]-1, 1)
    came_from, min_cost, good_endings = dfs(parsed,(start,Direction.E),end)
    paths = set()
    for e in good_endings:
        paths.update(find_paths(came_from, start, e))
    return paths,min_cost,parsed

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
    
    def __repr__(self):
        return {
            Direction.N:'North',
            Direction.E:'East',
            Direction.S:'South',
            Direction.W:'West'}[self]
    
class PriorityQueue:
    def __init__(self):
        self._elements = []

    def empty(self): return not self._elements

    def put(self, x, cost): heapq.heappush(self._elements, (cost,x))

    def get(self): return heapq.heappop(self._elements)[1]

def dfs(walls, start, end):
    frontier = PriorityQueue()
    frontier.put(start,0)
    # dict[Loc_Dir, Optional[Loc_Dir]]
    came_from = {}
    # dict[Loc_Dir, float]
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    # update when a minimum is found
    # end when no paths cost less
    min_cost = None

    while not frontier.empty():
        current = frontier.get()

        # only check loc, not dir
        if current[0] == end:
            if not min_cost:
                min_cost = cost_so_far[current]
            continue

        for next,cost in neighbors(current):
            if min_cost and cost > min_cost:
                # we're done, shut it down
                frontier = PriorityQueue()
                break
            # check not in a wall
            if next[0] in walls:
                continue
            new_cost = cost_so_far[current] + cost
            # if we haven't been here, or we're getting here cheaper
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                frontier.put(next,new_cost)
                came_from[next] = [current]
            # if we're getting here for equal cost
            elif cost_so_far[next] == new_cost:
                # cost is same, no update
                frontier.put(next,new_cost)
                came_from[next].append(current)
    
    good_endings = [e for e in came_from if e[0] == end and cost_so_far[e] == min_cost]
    return came_from, min_cost, good_endings

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
            ret += '#' if (i,j) in walls else 'O' if (i,j) in path else '.'
        ret += '\n'
    return ret

def part1(parsed):
    return parsed[1]

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