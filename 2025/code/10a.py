DAY = 10
YEAR = 2025

START = f'/workspaces/Advent of Code/{YEAR}'
SAMPLE_PATH = f'{START}/sample/{DAY}.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]
ALL = [SAMPLE_PATH, DATA_PATH]

RUN = ONLY_SAMPLE

# --------------------------------

from collections import namedtuple
from functools import cache
import pathlib
import sys

SAMPLE_ANSWER_1 = 7
SAMPLE_ANSWER_2 = 33

def parse(puzzle_input):
    machines = []
    for line in puzzle_input.splitlines():
        # parse the input
        # [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
        light_diagram = []
        buttons = []
        joltages = []
        for manual_item in line.split():
            match manual_item[0]:
                case '[':
                    manual_item = manual_item.strip('[]')
                    light_diagram = tuple([i == '#' for i in manual_item])
                case '(':
                    manual_item = manual_item.strip('()')
                    buttons.append(tuple([int(i) for i in manual_item.split(',')]))
                case '{':
                    manual_item = manual_item.strip('{}')
                    joltages = tuple([int(j) for j in manual_item.split(',')])
        machines.append(Machine(light_diagram, tuple(buttons), joltages))
    return machines

Machine = namedtuple('Machine', ['lights', 'buttons', 'joltages'])

@cache
def push_button(state,button):
    return tuple([not state[i] if i in button else state[i] for i in range(len(state))])

# all_buttons: collection of buttons
# pressed_buttons: equal len collection of T/F
@cache
def push(buttons, pushed, length):
    ret = tuple([False]*length)
    for i in range(len(buttons)):
        if pushed[i]:
            ret = push_button(ret,buttons[i])
    return tuple(ret)

@cache
def count_button(state,button):
    return tuple([state[i]+1 if i in button else state[i] for i in range(len(state))])

@cache
def count(buttons, pushed, length):
    ret = tuple([0]*length)
    for i in range(len(buttons)):
        if pushed[i]:
            ret = count_button(ret,buttons[i])
    return tuple(ret)

@cache
def all_press_combos(num_buttons):
    combos = 2**num_buttons
    def binary(n,l=None):
        r = []
        while n != 0:
            r.append(n%2)
            n = n//2
        if isinstance(l,int):
            while len(r) < l:
                r.append(0)
        return tuple(r)
    ret = []
    bin_num = binary(combos-1)
    b_length = len(bin_num)
    for num in range(combos):
        ret.append(binary(num,b_length))
    return tuple(ret)

def solve_lights(lights,buttons, verbose=False):
    m = len(buttons)+1
    mem = None
    for p in all_press_combos(len(buttons)):
        if lights == push(buttons,p,len(lights)):
            if sum(p) < m:
                m = sum(p)
                mem = p
            # m = min(m, sum(p))
    if verbose:
        print(f'solved got {mem}')
        print(f'pushed {lights}')
    return mem

def decimalized_joltage(joltages):
    decimal = 0
    val = 1
    for joltage in joltages:
        decimal += joltage * val
        val *= 10
    ret = [int(d) for d in str(decimal)]
    ret.reverse()
    return tuple(ret)

def joltage_to_light(joltages):
    ret = []
    for joltage in joltages:
        if joltage%2 == 0: ret.append(0)
        else: ret.append(1)
    return tuple(ret)

def shave_joltages(joltages,button_jolts):
    ret = []
    dec = decimalized_joltage(button_jolts)
    print(f'Really pushed {dec}')
    for i in range(len(joltages)):
        ret.append(joltages[i]-dec[i])
    return tuple(ret)

def halve_joltages(joltages):
    ret = []
    for joltage in joltages:
        assert joltage%2==0
        ret.append(joltage//2)
    return tuple(ret)

def part1(parsed):
    ret = 0
    for machine in parsed:
        ret += len(solve_lights(machine.lights,machine.buttons))
    return ret

def part2(parsed):
    ret = 0
    for machine in parsed:
        print(machine)
        r = 0
        joltages = decimalized_joltage(machine.joltages)
        print(f'start: {joltages}')
        pushes = solve_lights(joltage_to_light(joltages),machine.buttons,True)
        r += sum(pushes)
        push_jolt_count = count(machine.buttons, pushes, len(joltages))
        joltages = shave_joltages(joltages,push_jolt_count)
        print(f'shaved: {joltages}')
        joltages = halve_joltages(joltages)
        print(f'halved: {joltages}')
        while sum(joltages) > 0:
            pushes = solve_lights(joltage_to_light(joltages), machine.buttons,True)
            r += 2 * len(pushes)
            push_jolt_count = count(machine.buttons, pushes, len(joltages))
            joltages = shave_joltages(joltages,push_jolt_count)
            print(f'shaved: {joltages}')
            joltages = halve_joltages(joltages)
            print(f'halved: {joltages}')
        print(r)
        ret += r
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
