DAY = 11
YEAR = 2025

START = f'/workspaces/Advent of Code/{YEAR}'
SAMPLE_PATH = f'{START}/sample/{DAY}.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]
ALL = [SAMPLE_PATH, DATA_PATH]

RUN = ONLY_SAMPLE

# --------------------------------

import pathlib
import sys

SAMPLE_ANSWER_1 = 5
SAMPLE_ANSWER_2 = 2

def parse(puzzle_input):
    # parse the input
    d = {}
    for line in puzzle_input.splitlines():
        device, outputs = line.split(':')
        d.update({device:[o for o in outputs.strip().split()]})
    for r in range(20):
        print(f'{len([k for k in d if puzzle_input.count(k) > r])} over {r}')
    return d

def flood(map, start, goal):
    ret = 0
    frontier = []
    frontier.append(start)
    while len(frontier) != 0:
        device = frontier.pop(0)
        for next in map.get(device):
            if next == goal:
                ret += 1
            elif next == 'out':
                continue
            else:
                frontier.append(next)
    return ret

def flood_and_prune(map, start, goal,prunable=[]):
    ret = 0
    frontier = []
    reached = set()
    frontier.append(start)
    while len(frontier) != 0:
        device = frontier.pop(0)
        for next in map.get(device):
            if next == goal:
                ret += 1
            elif next in prunable:
                continue
            else:
                frontier.append(next)
                reached.add(next)
    return ret,reached

def flood_with_signal(map,start,visiting):
    frontier = []
    reached = {}
    frontier.append(start)
    reached.update({start:(1,[])})
    while len(frontier) != 0:
        device = frontier.pop(0)
        for next in map.get(device):
            temp = reached.get(next,(0,[]))
            if next == 'out':
                reached.update({next:(temp[0]+1,temp[1])})
                continue
            for visit in visiting:
                if next == visit:
                    reached.update({next:(temp[0]+1,temp[1]+[visit])})
                frontier.append(next)
                continue
            reached.update({next:(temp[0]+1,temp[1])})
            frontier.append(next)

# def dfs(map,start,goal,so_far=[]):
#     if start == goal:
#         return [so_far]
#     ret = []
#     so_far = so_far + [start]
#     for next in map.get(start):
#         ret += dfs(map,next,goal,so_far)
#     return ret

def shrink_graph(map,goal):pass

def part1(parsed):
    return flood(parsed,'you','out')

def part2(parsed):
    svr,dac,fft,out = ['svr','dac','fft','out']
    # dac -/-> fft
    paths = []
    # paths from dac --> out
    # 7957
    p,pruning = flood_and_prune(parsed,dac,out)
    paths.append(p)
    print(paths)
    return 0
    # paths from fft --> dac
    p,pruning = flood_and_prune(parsed,fft,dac,pruning)
    paths.append(p)
    print(paths)
    # paths from svr --> fft
    p,pruning = flood_and_prune(parsed,svr,fft,pruning)
    paths.append(p)
    print(paths)
    # print(f'{fft} -{flood(parsed,fft,dac)}-> {dac}')
    return paths[0]*paths[1]*paths[2]

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
