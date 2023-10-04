
import pathlib
import re
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

# Dictionary of Signal Objects, Key is Signal name
WIRE_DIAGRAM = {}

# Dictionary of already computed values
PRE_COMPUTES = {}

# one or two operands(string or value), an operation or None.
class Signal():
    def __init__(self, op1, op2, operation):
        self.op1 = op1
        self.op2 = op2
        self.operation = operation

    def eval(self, name):
        # print(f"Evaluating: {self.op1} {self.operation} {self.op2}")
        value1 = None
        try:
            value1 = int(self.op1)
        except:
            if self.op1 in PRE_COMPUTES.keys():
                value1 = PRE_COMPUTES[self.op1]
            else:
                value1 = Signal.eval(WIRE_DIAGRAM[self.op1])
        if (self.op2):
            value2 = None
            try:
                value2 = int(self.op2)
            except:
                if self.op2 in PRE_COMPUTES.keys():
                    value2 = PRE_COMPUTES[self.op2]
                else:
                    value2 = Signal.eval(WIRE_DIAGRAM[self.op2])
            if self.operation == "AND":
                ans = value1 & value2
                PRE_COMPUTES.update({name: ans})
                return ans
            if self.operation == "OR":
                ans = value1 | value2
                PRE_COMPUTES.update({name: ans})
                return ans
            if self.operation == "LSHIFT":
                ans = value1 << value2
                PRE_COMPUTES.update({name: ans})
                return ans
            if self.operation == "RSHIFT":
                ans = value1 >> value2
                PRE_COMPUTES.update({name: ans})
                return ans
            #return self.operation(value1, value2)
        if self.operation:
            return ~ value1
        return value1

def parse(puzzle_input):
    # ([operands{1/2, number or name}, func{None, AND, OR, LSHIFT, RSHIFT, NOT, }, ])

    for line in puzzle_input.split('\n'):
        # parse the input
        operation = None
        op1 = None
        op2 = None
        #destination is y
        (x, y) = line.split(" -> ")

        if len(y.split(" ")) > 1:
            print(y)
        ops = x.split(" ")
        if re.match("NOT", x):
            operation = ops[0]
            op1 = ops[1]
        elif re.search("AND", x) or re.search("OR", x) or re.search("LSHIFT", x) or re.search("RSHIFT", x):
            op1 = ops[0]
            operation = ops[1]
            op2 = ops[2]
        else:
            # print(f"{x} not a match...")
            op1 = ops[0]

        # get destination, insert into WIRE_DIAGRAM
        WIRE_DIAGRAM.update({y:Signal(op1, op2, operation)})
    return 0

def part1(parsed):
    # ret = {}
    # seeking = ['d', 'e', 'f', 'g', 'h', 'i', 'x', 'y']
    # for x in seeking:
    #     ret.update({x: Signal.eval(WIRE_DIAGRAM[x])})
    # return ret
    return Signal.eval(WIRE_DIAGRAM['a'])

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