from enum import Enum
import pathlib
import sys

SAMPLE_ANSWER_1 = 46
SAMPLE_ANSWER_2 = None

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
    lines = tuple(tuple(line) for line in puzzle_input.split())
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            tile_map.update({(x,y): CHAR_TO_TYPE.get(lines[x][y])})
    ret = Tile_Graph()
    for k in tile_map.keys():
        for v in [( 0,-1),( 0, 1),(-1, 0),( 1, 0)]:
            ret.add_edge((k, v), neighbors(tile_map, k, v))
    return ret

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