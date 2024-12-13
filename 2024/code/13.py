DAY = 13

START = f'/workspaces/Advent of Code/2024'
SAMPLE_PATH = f'{START}/sample/{DAY}.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]
ALL = [SAMPLE_PATH, DATA_PATH]

RUN = ONLY_DATA

# --------------------------------
import pathlib
import numpy as np
import re
import sys

SAMPLE_ANSWER_1 = 480
SAMPLE_ANSWER_2 = 875318608908

def parse(puzzle_input):
    # parse the inpu
    ret = []
    machines = [lines for lines in puzzle_input.split('\n\n')]
    for machine in machines:
        read = [int(x) for x in re.findall(r'\d+',machine)]
        ret.append(ClawMachine(*read))
    return ret

class ClawMachine():
    # prize : (x,y)
    # button a : (+x,+y)
    # button b : (+x,+y)
    def __init__(self,a_x,a_y,b_x,b_y,p_x,p_y):
        self._ax = a_x
        self._ay = a_y
        self._bx = b_x
        self._by = b_y
        self._px = p_x
        self._py = p_y

    def solve(self):
        # a_x*a + b_x*b = prize_x
        # a_y*a + b_y*b = prize_y
        a = np.array([[self._ax, self._bx], [self._ay, self._by]])
        b = np.array([self._px, self._py])
        return np.linalg.solve(a,b)

    def higher_prize(self):
        inc = 10000000000000
        self._px = self._px + inc
        self._py = self._py + inc

    def push_buttons(self, a, b):
        return (self._ax*a + self._bx*b,
                self._ay*a + self._by*b)

    def is_prize(self,a,b):
        return (self._px,self._py) == self.push_buttons(a,b)

    def __repr__(self):
        # Button A: X+94, Y+34
        # Button B: X+22, Y+67
        # Prize: X=8400, Y=5400
        return f'''
Button A: X+{self._button_a[0]}, Y+{self._button_a[1]}
Button B: X+{self._button_b[0]}, Y+{self._button_b[1]}
Prize: X={self._prize[0]}, Y={self._prize[1]}
'''

def get_prize(machine):
    a,b = [int(np.around(x)) for x in machine.solve()]
    if machine.is_prize(a,b):
        return b + a*3
    return False

def part1(parsed):
    # print(parsed)
    ret = 0
    for machine in parsed:
        tokens = get_prize(machine)
        if tokens:
            ret += tokens
    return ret

def part2(parsed):
    ret = 0
    for machine in parsed:
        machine.higher_prize()
        tokens = get_prize(machine)
        if tokens:
            ret += tokens
    return ret

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

def run(path):
    print(f'{path}')
    puzzle_input = pathlib.Path(path).read_text().strip()

    solutions = solve(puzzle_input)
    print('\n'.join(str(solution) for solution in solutions))

if __name__ == "__main__":
    for path in RUN:
        run(path)
    for path in sys.argv[1:]:
        run(path)