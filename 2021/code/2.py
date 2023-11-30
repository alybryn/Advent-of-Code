from enum import Enum
from pathlib import Path
import re
import sys

SAMPLE_ANSWER_1 = 150
SAMPLE_ANSWER_2 = 900

def parse(puzzle_input):
    # parse the input
    lines = [line for line in puzzle_input.split("\n")]
    
    #matcher = re.compile(r"((up)|(down)|(forward)) [0-9]")
    udf_matcher = re.compile(r"(up)|(down)|(forward)")
    num_matcher = re.compile(r"[a-z]* [0-9]")
    up_matcher = re.compile(r"up")
    down_matcher = re.compile(r"down")
    forward_matcher = re.compile(r"forward")
    
    for line in lines:
        print(udf_matcher.match(line))
        print(num_matcher.match(line))


class Instruction:
    directions = ['up', 'down', 'forward']
    class Direction(Enum):
        UP = 0
        DOWN = 1
        FORWARD = 2

    def __init__(self, dir: Direction, val: int) -> None:
        self._dir = dir
        self._val = val

def part1(parsed):
    return 0

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
        puzzle_input = Path(path).read_text().strip()

        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))