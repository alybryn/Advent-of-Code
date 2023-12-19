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
class MachinePart():
    def __init__(self, input) -> None:
        self._qualities = {}
        input = input.removeprefix('{').removesuffix('}').split(',')
        for i in input:
            self._qualities[Quality(i[0])] = int(i[2:])
            
    def get(self, q: Quality):
        return self._qualities[q]
    
    @property
    def value(self):
        ret = 0
        for q in Quality:
            ret += self._qualities[q]
        return ret

    def __repr__(self) -> str:
        return '{'+f'x={self._qualities[Quality.X]},m={self._qualities[Quality.M]},a={self._qualities[Quality.A]},s={self._qualities[Quality.S]}'+'}'

class Comparator():
    def __init__(self, q: str, c: str, n: str) -> None:
        self._q = Quality(q)
        self._c = Compare(c)
        self._n = int(n)

    def evaluate(self, part: MachinePart):
        return self._c.compare()(part.get(self._q), self._n)
        # part_value = part.get(self._q)
        # if self._c == Compare.MORE:
        #     return part_value > self._n
        # else:
        #     return part_value < self._n

    def __str__(self) -> str:
        return f'{self._q.value}{str(self._c)}{self._n}'

def parse(puzzle_input):
    # parse the input
    workflows, parts = puzzle_input.split('\n\n')
    workflows = workflows.split('\n')
    workflow_dict = {}
    for workflow in workflows:
        name, workflow = workflow.split('{')
        workflow = [w for w in workflow.removesuffix('}').split(',')]
        workflow_dict[name] = Workflow(workflow)
    parts = parts.split('\n')
    parts = [MachinePart(p) for p in parts]
    return workflow_dict, parts

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