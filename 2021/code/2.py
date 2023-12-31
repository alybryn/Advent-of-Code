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

class Direction(Enum):
    UP = 0
    DOWN = 1
    FORWARD = 2

class Instruction:
    def __init__(self, dir: str, val: int) -> None:
        self._dir = Direction[dir.upper()]
        self._val = val
    
    @property
    def dir(self):
        return self._dir

    @property
    def val(self):
        return self._val

class Submarine():
    def __init__(self, version = 1) -> None:
        self._version = version
        self._horizontal_position = 0
        self._depth = 0
        self._aim = 0
    
    @property
    def pos(self):
        return self._horizontal_position * self._depth

    def obey(self, instruction: Instruction):
        if instruction.dir == Direction.UP:
            if self._version == 1:
                self._depth -= instruction.val
            else:
                self._aim -= instruction.val
        elif instruction.dir == Direction.DOWN:
            if self._version == 1:
                self._depth += instruction.val
            else:
                self._aim += instruction.val
        else: # instruction.dir == Direction.FORWARD
            self._horizontal_position += instruction.val
            if self._version == 2:
                self._depth += instruction.val * self._aim

def loop(sub, parsed):
    for i in parsed:
        sub.obey(i)
    return sub.pos

def part1(parsed):
    my_sub = Submarine()
    return loop(my_sub, parsed)

def part2(parsed):
    my_sub = Submarine(2)
    return loop(my_sub, parsed)

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