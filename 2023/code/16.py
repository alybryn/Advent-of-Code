from enum import Enum
import pathlib
import sys

SAMPLE_ANSWER_1 = 46
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return tuple(tuple(line) for line in puzzle_input.split())

class NodeType(Enum):
    NONE = {( 0,-1): [( 0, 1)],
            ( 0, 1): [( 0,-1)],
            (-1, 0): [( 1, 0)],
            ( 1, 0): [(-1, 0)],
            }
    DASH = {( 0,-1): [( 0, 1)],
            ( 0, 1): [( 0,-1)],
            (-1, 0): [( 0,-1),( 0, 1)],
            ( 1, 0): [( 0,-1),( 0, 1)],
            }
    PIPE = {( 0,-1): [(-1, 0),( 1, 0)],
            ( 0, 1): [(-1, 0),( 1, 0)],
            (-1, 0): [( 1, 0)],
            ( 1, 0): [(-1, 0)],
            }
    BACK = {( 0,-1): [( 1, 0)],
            ( 0, 1): [(-1, 0)],
            (-1, 0): [( 0, 1)],
            ( 1, 0): [( 0,-1)],
            }
    FORE = {( 0,-1): [(-1, 0)],
            ( 0, 1): [( 1, 0)],
            (-1, 0): [ 0,-1],
            ( 1, 0): [ 0, 1],
            }

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