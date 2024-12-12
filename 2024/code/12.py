DAY = 12

START = f'/home/abi/Documents/programming/Advent of Code/2024'
SAMPLE_PATH = f'{START}/sample/{DAY}a.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]
ALL = [SAMPLE_PATH, DATA_PATH]

RUN = ONLY_SAMPLE

# --------------------------------

from enum import Enum
import pathlib
import sys

SAMPLE_ANSWER_1 = 1930
SAMPLE_ANSWER_2 = 1206

def parse(puzzle_input):
    # parse the input
    lines = [[l for l in line] for line in puzzle_input.splitlines()]

    field = []
    plotted = set()
    bounds = (len(lines)), len(lines[0])
    for i in range(0, bounds[0]):
        for j in range(0, bounds[1]):
            if (i,j) not in plotted:
                plot = travel_plot(lines,bounds,lines[i][j],(i,j))
                # add to visited
                plotted = plotted.union(plot.locs)
                field.append(plot)
    return field

def travel_plot(lines,bounds, name, start):
    visited = {start}
    plotted = {start}
    to_search = [start]
    while to_search:
        next = to_search.pop()
        for adj in adjacent(next):
            if adj not in visited:
                if 0 <= adj[0] < bounds[0] and 0 <= adj[1] < bounds[1]:
                    visited.add(adj)
                    if lines[adj[0]][adj[1]] == name:
                        plotted.add(adj)
                        to_search.append(adj)
    plot = Plot(name, plotted)
    return plot

def adjacent(loc):
    return[(loc[0]+dir.value[0],loc[1]+dir.value[1]) for dir in Direction]
    
class Plot():
    def __init__(self,name,locs):
        self.name = name
        self._locs = locs
        self._area = len(self._locs)
        self._outside = [adj 
                         for loc in self._locs 
                         for adj in adjacent(loc) 
                         if adj not in self._locs]
        self._perimeter = len(self._outside)
        self._sides = self.walk_sides()
    
    def walk_sides(self):
        to_visit = set(self._outside)
        num_sides = 0
        visited = set()
        # keep going to find interior fences
        while len(to_visit.difference(visited)) != 0:
            num_sides +=1
            # inside is the direction of fence
            inside = Direction.S
            # dir is the direction of travel
            dir = Direction.E
            # stop_dir is direction when stopping
            stop_dir = Direction.N
            # start should be the farthest north and west
            # square outside the plot
            start = min(to_visit.difference(visited))
            # last is kitty corner, south and west
            # keep track of outside visited:
            last = (start[0]+Direction.S.value[0]+Direction.W.value[0], 
                    start[1]+Direction.S.value[1]+Direction.W.value[1])
            # if start.North IS inside, turn the whole car around
            if (start[0]+Direction.N.value[0], start[1]+Direction.N.value[1]) in self._locs:
                inside = Direction.W
                dir = Direction.S
                stop_dir = Direction.W
                last = start
            visited.add(start)
            # set a cursor
            curr = start
            # make one loop
            while not (curr == last and dir == stop_dir):
                # if direction of travel inside:
                if (curr[0] + dir.value[0], curr[1] + dir.value[1]) in self._locs:
                    # turn left, increment sides
                    inside = inside.turn_left()
                    dir = dir.turn_left()
                    num_sides += 1
                    continue
                # forward step
                step = (curr[0]+dir.value[0],curr[1]+dir.value[1])
                kitty = (step[0]+inside.value[0], step[1]+inside.value[1])
                # if kitty-corner outside:
                if kitty not in self._locs:
                    # turn right, increment sides
                    inside = inside.turn_right()
                    dir = dir.turn_right()
                    num_sides += 1
                    curr = kitty
                # else
                else:
                    # step forward
                    curr = step
                visited.add(curr)
        return num_sides

    @property
    def locs(self):
        return self._locs
    
    @property
    def area(self):
        return self._area
    
    @property
    def perimeter(self):
        return self._perimeter
    
    @property
    def sides(self):
        return self._sides

class Direction(Enum):
    N = (-1, 0)
    S = ( 1, 0)
    E = ( 0, 1)
    W = ( 0,-1)
    
    def turn_right(self):
        ret = {Direction.N:Direction.E,
        Direction.E:Direction.S,
        Direction.S:Direction.W,
        Direction.W:Direction.N}
        return ret[self]
    
    def turn_left(self):
        ret = {Direction.N:Direction.W,
        Direction.W:Direction.S,
        Direction.S:Direction.E,
        Direction.E:Direction.N}
        return ret[self]

def part1(parsed):
    # print(parsed)
    ret = 0
    for plot in parsed:
        ret += plot.area * plot.perimeter
    return ret

def part2(parsed):
    ret = 0
    for plot in parsed:
        ret += plot.area * plot.sides
    return ret

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