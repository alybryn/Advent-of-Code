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

from functools import cache
import pathlib
import sys

SAMPLE_ANSWER_1 = 7
SAMPLE_ANSWER_2 = None

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
                    joltages = [int(j) for j in manual_item.split(',')]
        machines.append(Machine(light_diagram, buttons, joltages))
    return machines

@cache
def push(button, lights):
    return tuple([not lights[i] if i in button else lights[i] for i in range(len(lights))])

class Machine:
    def __init__(self, lights, buttons, joltages):
        self._pattern = lights
        self._buttons = buttons
        self._joltages = joltages
        self._button_costs = [sum([joltages[i] for i in button]) for button in buttons]
    
    def is_start_state(self, p):
        return p == self._pattern
    
    # given an incoming lighting diagram
    # return a list of lighting diagrams for pushing each button once
    def push_all_buttons(self,lights):
        ret = []
        for button in self._buttons:
            ret.append(push(button,lights))
        return ret

    def get_num_lights(self):
        return len(self._pattern)

    def __repr__(self):
        pattern = ''.join(['#'  if p else '.' for p in self._pattern])
        buttons = ' '.join([f'({','.join([str(b) for b in button])})' for button in self._buttons])
        joltages = '{'+f'{','.join([str(j) for j in self._joltages])}'+'}'
        button_costs = ' '.join([str(cost) for cost in self._button_costs])
        return f'{pattern} {buttons} {joltages} {button_costs}'

def part1(parsed):
    ret = 0
    for machine in parsed:
        lights = [tuple([False]*machine.get_num_lights())]
        presses = 0
        while True not in [machine.is_start_state(l) for l in lights]:
            next_state = []
            for l in lights:
                next_state += machine.push_all_buttons(l)
            presses += 1
            lights = next_state
        ret += presses
    return ret

def part2(parsed):
    # prediction: have to minimize the energy use instead of the button presses
    # energy use is how much joltage used to turn a light on or off
    print(f'{'\n'.join([str(m) for m in parsed])}')
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
