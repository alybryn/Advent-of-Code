DAY = 21

START = f'workspaces/Advent of Code/2024'
SAMPLE_PATH = f'{START}/sample/{DAY}.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]
ALL = [SAMPLE_PATH, DATA_PATH]

RUN = ONLY_SAMPLE

# --------------------------------

import pathlib
import sys

SAMPLE_ANSWER_1 = 126384
SAMPLE_ANSWER_2 = None

NumbericPadNeighbors = {
    '7':['8','4'],'8':['7','5','9'],'9':['8','6'],
    '4':['7','5','1'],'5':['4','8','6','2'],'6':['5','9','3'],
    '1':['4','2'],'2':['1','5','3','0'],'3':['2','6','A'],
    '0':['2','A'],'A':['0','3']}

DirectionalPadNeighbors = {
    '^':['A','v'],'A':['^','>'],
    '<':['v'],'v':['<','^','>'],'>':['A','v']
}

def parse(puzzle_input):
    # parse the input
    return [line for line in puzzle_input.splitlines()]

def complexity(code):
    num = int(code[:-1])
    num_robot = shortest_buttons(code, NumbericPadNeighbors)
    dir_robot_1 = shortest_buttons(num_robot, DirectionalPadNeighbors)
    my_buttons = shortest_buttons(dir_robot_1, DirectionalPadNeighbors)
    return len(my_buttons) * num

def shortest_buttons(code, neighbors):
    curr = 'A'

def part1(parsed):
    print(parsed)
    ret = 0
    for code in parsed:
        ret += complexity(code)
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