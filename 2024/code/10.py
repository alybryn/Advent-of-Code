DAY = 10

SAMPLE_PATH = f'sample/{DAY}.txt'
DATA_PATH = f'data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]
ALL = [SAMPLE_PATH, DATA_PATH]

RUN = ONLY_ARGS

# --------------------------------

import pathlib
import sys

SAMPLE_ANSWER_1 = 36
SAMPLE_ANSWER_2 = 81

def parse(puzzle_input):
    # parse the input
    map = {}
    puzzle_input = [[int(l) for l in line] for line in puzzle_input.splitlines()]
    for i in range(0,len(puzzle_input)):
        for j in range(0,len(puzzle_input[0])):
            # store p_i[i][j]:.add(i,j)
            s = map.get(puzzle_input[i][j],set())
            s.add((i,j))
            map.update({puzzle_input[i][j]:s})
    return map

def adjacent(point):
    vectors = [(0,-1),(0,1),(-1,0),(1,0)]
    return [(point[0]+v[0],point[1]+v[1]) for v in vectors]

def find_trailheads(map):
    return [(i,j) for i,m in enumerate(map) for j,n in enumerate(m) if n == 0]

def score(map, trailhead):
    explored = {trailhead}
    # change elevation from 0 -> 9
    for l in range(0, 9):
        if len(explored) == 0:
            return 0
        new_level = set()
        for loc in explored:
            new_level = new_level.union(step_up(map, loc, l))
        explored = new_level
    return len(explored)

def step_up(map, loc, level):
    ret = set()
    # neighbors of location
    for n in adjacent(loc):
        # if the neighbor is one step up
        if n in map.get(level+1,set()):
            ret.add(n)
    # progress to next level
    return ret

def rate(map, trailhead):
    explored = [trailhead]
    # change elevation from 0 -> 9
    for l in range(0, 9):
        if len(explored) == 0:
            return 0
        new_level = []
        for loc in explored:
            new_level += step_up(map, loc, l)
        explored = new_level
    return len(explored)

def part1(parsed):
    trailheads = parsed.get(0)
    c = 0
    for trailhead in trailheads:
        c += score(parsed, trailhead)
    return c

def part2(parsed):
    trailheads = parsed.get(0)
    c = 0
    for trailhead in trailheads:
        c += rate(parsed, trailhead)
    return c

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