from collections import namedtuple
from queue import PriorityQueue
import pathlib
import sys

SAMPLE_ANSWER_1 = 102
SAMPLE_ANSWER_2 = None

INF_COST = 1000000000000

def parse(puzzle_input):
    # parse the input
    ret = {}
    lines = [[int(l) for l in list(line)] for line in puzzle_input.split()]
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            ret.update({Block(x, y): lines[x][y]})
    return CityMap(ret, len(lines), len(lines[0]))

Bounds = namedtuple('Bounds', ['min_x', 'max_x', 'min_y', 'max_y'])

class Block(namedtuple('Block', ['x', 'y'])):
    def __repr__(self) -> str:
        return f'({self.x},{self.y})'

class CityMap():
    def __init__(self, blocks, max_x, max_y, min_y=0, min_x=0) -> None:
        self._heat_map = blocks
        self._dimensions = Bounds(min_x, max_x, min_y, max_y)
        self._edges = {}

        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                # self._edges.update({Block(x, y):[Block(x  ,y-1),
                #                                  Block(x  ,y+1),
                #                                  Block(x-1,y  ),
                #                                  Block(x+1,y  )
                #                                  ]})
                self._edges.update({Block(x,y):[(Block(x  ,y-1),'<'),
                                                (Block(x  ,y+1),'>'),
                                                (Block(x-1,y  ),'^'),
                                                (Block(x+1,y  ),'v')
                                                ]})

    @property
    def start(self):
        return Block(self._dimensions.min_x, self._dimensions.min_y)

    @property
    def end(self):
        return Block(self._dimensions.max_x - 1, self._dimensions.max_y - 1)

    def neighbors(self, block):
        return self._edges.get(block)

    def cost(self, from_blocks, to_block):
        # this is where the ring of fire goes...
        return self._heat_map.get(to_block, INF_COST)
    
    def __str__(self) -> str:
        p = ''
        for x in range(self._dimensions.min_x, self._dimensions.max_x):
            for y in range(self._dimensions.min_y, self._dimensions.max_y):
                p += str(self._heat_map.get((x, y)))
            p += '\n'
        return p
    
# PriorityQueue: put((cost, item)), get(), empty()

def a_star(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put((0,start))
    came_from = {}
    cost_so_far = {}
    directions = {}
    came_from[start] = None
    cost_so_far[start] = 0
    directions[start] = None

    while frontier.qsize() != 0:
        pri, current = frontier.get()
        print(f'({current})')
        # print_visited(came_from)
        # print(cost_so_far[current])
        if current == goal:
            comprehensive_print(came_from, cost_so_far, current)
            return cost_so_far[current]
        
        # create list of last three dirs
        prev1 = came_from.get(current)
        prev2 = came_from.get(prev1)
        prev3 = came_from.get(prev2)
        prev = [directions.get(current), directions.get(prev1), directions.get(prev2)]#, directions.get(prev3)]
        print(current, prev1, prev2)#, prev3)
        print(prev)

        # print(f'neighbors: {graph.neighbors(current)}')
        # next is ((x,y), '[<|>|^|v]')
        for next, dir in graph.neighbors(current):
            print(next)
            if next == came_from[current]:
                continue

            if prev.count(dir) == 3:
                continue

            new_cost = cost_so_far[current] + graph.cost(prev, next)
            print(new_cost)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost #+ heuristic(goal, next)
                frontier.put((priority, next))
                came_from[next] = current
                directions[next] = dir

def heuristic(goal: Block, next: Block):
    return manhattan_distance(goal, next)

def manhattan_distance(a: Block, b: Block):
    return abs(a.x - b.x) + abs(a.y - b.y)

def print_path(graph, last):
    print('printing path')
    while graph[last]:
        print(graph[last])
        last = graph[last]

def print_visited(came_from):
    p = ''
    for x in range(12):
        for y in range(12):
            p += '#' if (x,y) in came_from else '.'
        p += '\n'
    print(p)

def at_what_cost(cost_so_far):
    for x in range(12):
        for y in range(12):
            print(f'({x},{y}): {cost_so_far.get((x,y),0)}')

def comprehensive_print(came_from, cost_so_far, last):
    while came_from[last]:
        print(f'{came_from[last]} -> {last} costs {cost_so_far[last]}')
        last = came_from[last]

def part1(parsed):
    return a_star(parsed, parsed.start, parsed.end)

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