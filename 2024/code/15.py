DAY = 15

START = f'/workspaces/Advent of Code/2024'
SAMPLE_PATH = f'{START}/sample/{DAY}.txt'
SAMPLE_PATH_A = f'{START}/sample/{DAY}a.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH,SAMPLE_PATH_A]
ONLY_DATA = [DATA_PATH]
ALL = ONLY_SAMPLE + ONLY_DATA

RUN = ONLY_SAMPLE

# --------------------------------

import pathlib
import sys

SAMPLE_ANSWER_1 = 10092, 2028
SAMPLE_ANSWER_2 = None

ROBOT = '@'
WALL = '#'
BOX = 'O'

Direction = {'^': ( 0,-1),
             'v': ( 0, 1),
             '<': (-1, 0),
             '>': ( 1, 0)}

def parse(puzzle_input):
    # parse the input
    state, moves = puzzle_input.split('\n\n')
    state_dict = {WALL:set(), BOX:set(), ROBOT:set()}
    # moves = moves.replace('\n', '')
    moves = [Direction[move] for move in moves if move in Direction]
    state = [s for s in state.splitlines()]
    for i in range(0, len(state)):
        for j in range(0,len(state[0])):
            if state[i][j] in state_dict:
                temp = state_dict[state[i][j]]
                temp.add((i,j))
                state_dict[state[i][j]] = temp
    return State(state_dict,(len(state),len(state[0]))), moves

class State():
    def __init__(self, state, bounds):
        self._reset = state
        self._boxes = state[BOX]
        self._walls = state[WALL]
        self._robot = state[ROBOT]
        self._bounds = bounds

    def reset(self):
        self._boxes = self._reset[BOX]
        self._walls = self._reset[WALL]
        self._robot = self._reset[ROBOT]

    def move(self, instruction):
        pass

    def __repr__(self):
        ret = ''
        for j in range(0,self._bounds[1]):
            for i in range(0, self._bounds[0]):
                if (i,j) in self._boxes:
                    ret += 'O'
                elif (i,j) in self._walls:
                    ret += '#'
                elif (i,j) in self._robot:
                    ret += '@'
                else:
                    ret += '.'
            ret += '\n'
        return ret

def part1(parsed):
    print(parsed)
    state, moves = parsed
    for move in moves:
        state.move(move)
    return state

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