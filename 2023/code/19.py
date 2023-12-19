from collections import namedtuple
import pathlib
from enum import Enum
import sys

SAMPLE_ANSWER_1 = 19114
SAMPLE_ANSWER_2 = None

class Quality(str, Enum):
    X = 'x'
    M = 'm'
    A = 'a'
    S = 's'

class Compare(str,Enum):
    LESS = '<'
    MORE = '>'

    def compare(self):
        match self:
            case Compare.LESS:
                return lambda m, w: m < w
            case Compare.MORE:
                return lambda m, w: m > w

    def __str__(self) -> str:
        return self.value

class CompDest(namedtuple('CompDest', ['comp', 'dest'])):
    def __repr__(self) -> str:
        return f'{str(self.comp)}:{self.dest}'

class Workflow():
    # input is [Quality'[>|<]:'GoTo,...,Default]
    def __init__(self, input) -> None:
        # list of namedtuples (Comparator, str)
        self.qualifications: [CompDest] = []
        self._default = 'R'
        for i in input:
            if ':' in i:
                comp, dest = i.split(':')
                self.qualifications.append(CompDest(Comparator(comp[0], comp[1], comp[2:]),dest))
            else:
                #default
                self._default = i

    def evaluate(self, part):
        for qualification in self.qualifications:
            if qualification.comp.evaluate(part):
                return qualification.dest
        return self._default
    def __repr__(self) -> str:
        return f'{str(self.qualifications)},{self._default}'
        
def parse(puzzle_input):
    # parse the input
    return [line for line in puzzle_input.split()]

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