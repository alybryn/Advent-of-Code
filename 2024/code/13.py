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
import re
import sys

SAMPLE_ANSWER_1 = 480
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the inpu
    ret = []
    machines = [lines for lines in puzzle_input.split('\n\n')]
    for machine in machines:
        a_x,a_y,b_x,b_y,p_x,p_y = [int(x) for x in re.findall(r'\d+',machine)]
        ret.append(ClawMachine((p_x,p_y),(a_x,a_y),(b_x,b_y)))
    return ret

class ClawMachine():
    # prize : (x,y)
    # button a : (+x,+y)
    # button b : (+x,+y)
    def __init__(self, prize, button_a, button_b):
        self._prize = prize
        self._button_a = button_a
        self._button_b = button_b

    # a button costs 3, b button costs 1
    # def get_prize(self, ptr=(0,0),spent=0):
    #     pass
    #     if ptr == self._prize:
    #         return spent
        # try to push b

        # try to push a

    # def push_button_a(self, ptr):
    #     return (ptr[0]+self._button_a[0],ptr[1]+self._button_a[1])

    # def push_button_b(self, ptr):
    #     return (ptr[0]+self._button_b[0],ptr[1]+self._button_b[1])

    def push_button_a(self,times,ptr):
        return (ptr[0] + self._button_a[0]*times,ptr[1] + self._button_a[1]*times)

    def push_button_b(self,times,ptr):
        return (ptr[0] + self._button_b[0]*times, ptr[1] + self._button_b[1]*times)

    def __repr__(self):
        # Button A: X+94, Y+34
        # Button B: X+22, Y+67
        # Prize: X=8400, Y=5400
        return f'''
Button A: X+{self._button_a[0]}, Y+{self._button_a[1]}
Button B: X+{self._button_b[0]}, Y+{self._button_b[1]}
Prize: X={self._prize[0]}, Y={self._prize[1]}
'''

def get_prize_looping(machine):
    for a in range(0,101):
        for b in range(0,101):
            ptr = (0,0)
            ptr = machine.push_button_a(a,ptr)
            ptr = machine.push_button_b(b,ptr)
            if machine.is_prize(ptr):
                return b + a*3
    return False



# def get_prize(machine, ptr=(0,0),a=0,b=0):
#     if machine.is_prize(ptr):
#         return (a*3)+b
#     if machine.overshot(ptr) or a>100 or b>100:
#         return None
#     a_move = machine.push_button_a(ptr)
#     b_move = machine.push_button_b(ptr)
#     a_cost = get_prize(machine,a_move,a+1,b)
#     b_cost = get_prize(machine,b_move,a,b+1)
#     if a_cost and b_cost:
#         return min(a_cost,b_cost)
#     if a_cost:
#         return a_cost
#     return b_cost

def part1(parsed):
    print(parsed)
    ret = 0
    for machine in parsed:
        tokens = get_prize_looping(machine)
        if tokens:
            ret += tokens
    return ret

def part2(parsed):
    return 0

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