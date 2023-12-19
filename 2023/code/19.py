from collections import namedtuple
import pathlib
from enum import Enum
import sys

SAMPLE_ANSWER_1 = 19114
SAMPLE_ANSWER_2 = 167409079868000

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
    
class RangeSplitResult(namedtuple('RangeSplitResult',['passing','failing'])):
    def __repr__(self) -> str:
        return f'pass: {self.passing}; fail: {self.failing}'

class WorkflowSplitResult(namedtuple('WorkflowSplitResult',['dest','part_range'])):
    def __repr__(self) -> str:
        return f'{self.dest}: {self.part_range}'

class Workflow():
    # input is [Quality'[>|<]:'GoTo,...,Default]
    def __init__(self, input) -> None:
        # list of namedtuples (Comparator, str)
        self._qualifications: [CompDest] = []
        self._default = 'R'
        for i in input:
            if ':' in i:
                comp, dest = i.split(':')
                self._qualifications.append(CompDest(Comparator(comp[0], comp[1], comp[2:]),dest))
            else:
                #default
                self._default = i

    def evaluate(self, part):
        for qualification in self._qualifications:
            if qualification.comp.evaluate(part):
                return qualification.dest
        return self._default
    
    def split(self, range):
        ret = set()
        for compdest in self._qualifications:
            split = range.split(compdest.comp)
            range = split.failing
            ret.add(WorkflowSplitResult(compdest.dest,split.passing))

        # sometimes, _default might already be a key...
        ret.add(WorkflowSplitResult(self._default, range))
        return ret

    def __repr__(self) -> str:
        return f'{str(self._qualifications)},{self._default}'

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

class ValueRange():
    def __init__(self,low=1,high=4000) -> None:
        self._low = low
        self._high = high

    def split(self, comp):
        match comp.comparator:
            case Compare.LESS:
                return RangeSplitResult(ValueRange(self._low, comp.value-1),ValueRange(comp.value, self._high))
            case Compare.MORE:
                return RangeSplitResult(ValueRange(comp.value+1, self._high),ValueRange(self._low, comp.value))
    
    @property
    def value(self):
        return self._high - self._low + 1
    
    def __repr__(self) -> str:
        return f'{self._low}->{self._high}'

class PartRange():
    # xmas are ValueRanges
    def __init__(self, x=ValueRange(), m=ValueRange(), a=ValueRange(), s=ValueRange()) -> None:
        self._qualities = {}
        self._qualities[Quality.X] = x
        self._qualities[Quality.M] = m
        self._qualities[Quality.A] = a
        self._qualities[Quality.S] = s

    def split(self, comp):
        result = self._qualities[comp.quality].split(comp)
        match comp.quality:
            case Quality.X:
                return RangeSplitResult(PartRange(result.passing, self._qualities[Quality.M], self._qualities[Quality.A], self._qualities[Quality.S]),PartRange(result.failing, self._qualities[Quality.M], self._qualities[Quality.A], self._qualities[Quality.S]))
            case Quality.M:
                return RangeSplitResult(PartRange(self._qualities[Quality.X], result.passing, self._qualities[Quality.A], self._qualities[Quality.S]),PartRange(self._qualities[Quality.X], result.failing, self._qualities[Quality.A], self._qualities[Quality.S]))
            case Quality.A:
                return RangeSplitResult(PartRange(self._qualities[Quality.X], self._qualities[Quality.M], result.passing, self._qualities[Quality.S]),PartRange(self._qualities[Quality.X], self._qualities[Quality.M], result.failing, self._qualities[Quality.S]))
            case Quality.S:
                return RangeSplitResult(PartRange(self._qualities[Quality.X], self._qualities[Quality.M], self._qualities[Quality.A], result.passing),PartRange(self._qualities[Quality.X], self._qualities[Quality.M], self._qualities[Quality.A], result.failing))

    @property
    def value(self):
        x = self._qualities[Quality.X].value
        m = self._qualities[Quality.M].value
        a = self._qualities[Quality.A].value
        s = self._qualities[Quality.S].value
        return x * m * a * s
    
    def __repr__(self) -> str:
        return f'x:{self._qualities[Quality.X]},m:{self._qualities[Quality.M]},a:{self._qualities[Quality.A]},s:{self._qualities[Quality.S]}'

class Comparator():
    def __init__(self, q: str, c: str, n: str) -> None:
        self._q = Quality(q)
        self._c = Compare(c)
        self._n = int(n)

    def evaluate(self, part: MachinePart):
        return self._c.compare()(part.get(self._q), self._n)

    @property
    def value(self):
        return self._n
    
    @property
    def comparator(self):
        return self._c
    
    @property
    def quality(self):
        return self._q

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
    workflows, parts = parsed
    ret = 0
    for part in parts:
        wf = workflows['in'].evaluate(part)
        while wf not in ['R','A']:
            wf = workflows[wf].evaluate(part)
        if wf == 'A':
            ret += part.value
    return ret

def part2(parsed):
    workflows, _ = parsed
    # list of PartRanges
    accepted_ranges = []
    # list of sets of WorkflowSplitResults(str, PartRange)
    ranges = [workflows['in'].split(PartRange())]
    while ranges:
        new_ranges = []
        for range_set in ranges:
            for wsr in range_set:
                if wsr.dest == 'A':
                    accepted_ranges.append(wsr.part_range)
                elif wsr.dest == 'R':
                    continue
                else:
                    new_ranges.append(workflows[wsr.dest].split(wsr.part_range))
           
        ranges = new_ranges
    return sum([r.value for r in accepted_ranges])

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