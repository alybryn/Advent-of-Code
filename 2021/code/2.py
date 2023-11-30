from enum import Enum
from pathlib import Path
import re
import sys

SAMPLE_ANSWER_1 = 150
SAMPLE_ANSWER_2 = 900

def parse(puzzle_input):
    ret = []
    # parse the input
    lines = [line for line in puzzle_input.split("\n")]
    
    pattern = r"(?P<dir>(up)|(down)|(forward)) (?P<val>[0-9])"
    
    for line in lines:
        #print(udf_matcher.match(line))
        if (match := re.match(pattern, line)):
            inst_dict = match.groupdict()
            ret.append(Instruction(inst_dict['dir'], int(inst_dict['val'])))
        else:
            print(f"uhoh, parse({line})")
    
    return ret


class Instruction:
    class Direction(Enum):
        UP = 0
        DOWN = 1
        FORWARD = 2

    def __init__(self, dir: str, val: int) -> None:
        self._dir = self.Direction[dir.upper()]
        self._val = val
    
    @property
    def dir(self):
        return self._dir

    @property
    def val(self):
        return self._val

def part1(parsed):
    for p in parsed:
        print(f"Instruction: {p.dir} {p.val}")
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