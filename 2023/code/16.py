from collections import deque
from enum import Enum
import pathlib
import sys

SAMPLE_ANSWER_1 = 46
SAMPLE_ANSWER_2 = 51

class NodeType(Enum):
    # incoming vector from last cell perspective.
    # (0,1) in will be (0,1) out unless acted upon
    NONE = {( 0,-1): [( 0,-1)],
            ( 0, 1): [( 0, 1)],
            (-1, 0): [(-1, 0)],
            ( 1, 0): [( 1, 0)],
            }
    DASH = {( 0,-1): [( 0,-1)],
            ( 0, 1): [( 0, 1)],
            (-1, 0): [( 0,-1),( 0, 1)],
            ( 1, 0): [( 0,-1),( 0, 1)],
            }
    PIPE = {( 0,-1): [(-1, 0),( 1, 0)],
            ( 0, 1): [(-1, 0),( 1, 0)],
            (-1, 0): [(-1, 0)],
            ( 1, 0): [( 1, 0)],
            }
    BACK = {( 0,-1): [(-1, 0)],
            ( 0, 1): [( 1, 0)],
            (-1, 0): [( 0,-1)],
            ( 1, 0): [( 0, 1)],
            }
    FORE = {( 0,-1): [( 1, 0)],
            ( 0, 1): [(-1, 0)],
            (-1, 0): [( 0, 1)],
            ( 1, 0): [( 0,-1)],
            }
    
CHAR_TO_TYPE = {'.': NodeType.NONE,
                '\\': NodeType.BACK,
                '/': NodeType.FORE,
                '-': NodeType.DASH,
                '|': NodeType.PIPE,
                }

def parse(puzzle_input):
    # parse the input
    tile_map = {}
    edges = []
    lines = tuple(tuple(line) for line in puzzle_input.split())
    for x in range(len(lines)):
        # add an edge for maxy, v = (0,-1) and miny (0,1)
        edges.append(((x,0), (0,1)))
        edges.append(((x,len(lines[0])-1),(0,-1)))
        for y in range(len(lines[0])):
            tile_map.update({(x,y): CHAR_TO_TYPE.get(lines[x][y])})
    for y in range(len(lines[0])):
        edges.append(((0,y),(1,0)))
        edges.append(((y,len(lines)-1),(-1,0)))
    graph = Tile_Graph()
    for k in tile_map.keys():
        for v in [( 0,-1),( 0, 1),(-1, 0),( 1, 0)]:
            graph.add_edge((k, v), neighbors(tile_map, k, v))
    return graph, edges

# returns [(loc, vector),...]; ((x,y), vector) for each neighbor
def neighbors(tile_map, loc, in_vector):
    out_vectors = tile_map.get(loc).value.get(in_vector)
    ret = []
    for v in out_vectors:
        n = (loc[0] + v[0], loc[1] + v[1])
        if n in tile_map.keys():
            ret.append(((loc[0] + v[0], loc[1] + v[1]), v))
    return ret

class Tile_Graph():
    def __init__(self) -> None:
        # edge is dict (loc, vec) -> [(loc,vec)]
        self._edges = {}
    
    # id is ((x,y),v)
    def neighbors(self, id):
        return self._edges[id]
    
    def add_edge(self, start, end):
        self._edges.update({start: end})

def bfs(graph: Tile_Graph, start):
    # frontier is queue
    frontier = deque()
    # put start in frontier
    frontier.append(start)
    # reached is a set
    reached = set()
    # put start in reached
    reached.add(start)
    # while frontier not empty:
    while frontier:
        # get an element from frontier
        element = frontier.popleft()
        # print(element)
        # iterate on neighbors of that element
        for neighbor in graph.neighbors(element):
            # if neighbor not in reached
            if neighbor not in reached:
                # print(f'\t{element}')
                # put neighbor in frontier
                frontier.append(neighbor)
                # put neighbor in reached
                reached.add(neighbor)
    #return reached
    return reached

def simplify_reached(reached):
    ret = {}
    for element in reached:
        count = ret.get(element[0], 0)
        count += 1
        ret.update({element[0]: count})
    return ret

def part1(parsed):
    graph = parsed[0]
    start = ((0,0), (0,1))
    reached = bfs(graph, start)
    reached = simplify_reached(reached)
    return len(reached)

def part2(parsed):
    graph, edges = parsed
    most = 0
    # for edge ((x,y),v):
    for edge in edges:
        # if len(simplify_reached(dfs(parsed, edge)) > most
        l = len(simplify_reached(bfs(graph, edge)))
        if  l > most:
            most = l
    return most

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