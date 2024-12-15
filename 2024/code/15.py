DAY = 15

START = f'/workspaces/Advent of Code/2024'
SAMPLE_PATH = f'{START}/sample/{DAY}.txt'
SAMPLE_PATH_A = f'{START}/sample/{DAY}a.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH_A, SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]
ALL = ONLY_SAMPLE + ONLY_DATA

RUN = ONLY_SAMPLE

# --------------------------------

import pathlib
import sys

SAMPLE_ANSWER_1 = 2028, 10092
SAMPLE_ANSWER_2 = 1806, 9021

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
    for j in range(0, len(state)):
        for i in range(0,len(state[0])):
            if state[j][i] in state_dict:
                temp = state_dict[state[j][i]]
                temp.add((i,j))
                state_dict[state[j][i]] = temp
    return Warehouse_1(state_dict,(len(state),len(state[0]))), Warehouse_2(state_dict,(len(state),len(state[0]))), moves

class Warehouse_1():
    def __init__(self, state, bounds):
        self._boxes = state[BOX]
        self._walls = state[WALL]
        self._robot = state[ROBOT].pop()
        state[ROBOT].add(self._robot)
        self._bounds = bounds

    def move_robot(self, instruction):
        proposed_loc = coord_add(self._robot, instruction)
        if proposed_loc not in self._boxes and proposed_loc not in self._walls:
            # way is clear
            self._robot = proposed_loc
        if proposed_loc in self._walls:
            # can't move
            return
        elif proposed_loc in self._boxes:
            # track the first box
            move_to = proposed_loc
            # move pointer until free space or wall
            while move_to in self._boxes:
                move_to = coord_add(move_to,instruction)
            # make a decision
            if move_to in self._walls:
                # can't move
                return
            # move the boxes... which just means moving one box...
            # remove box at to_move, add box at proposed_loc
            self._boxes.remove(proposed_loc)
            self._boxes.add(move_to)
            # move the robot
            self._robot = proposed_loc

    @property
    def gps_sum(self):
        ret = 0
        for box in self._boxes:
            ret += box[0] + box[1]*100
        return ret

    def __repr__(self):
        ret = ''
        for j in range(0,self._bounds[0]):
            for i in range(0, self._bounds[1]):
                if (i,j) in self._boxes:
                    ret += 'O'
                elif (i,j) in self._walls:
                    ret += '#'
                elif (i,j) == self._robot:
                    ret += '@'
                else:
                    ret += '.'
            ret += '\n'
        return ret

class Warehouse_2():
    def __init__(self, state, bounds):
        self._walls = set().union([(i*2,j)for i,j in state[WALL]]+[(i*2+1,j)for i,j in state[WALL]])
        self._boxes = set().union((i*2,j) for i,j in state[BOX])
        self._robot = state[ROBOT].pop()
        self._robot = (self._robot[0]*2, self._robot[1])
        self._bounds = (bounds[0],bounds[1]*2)

    def move_robot(self, instruction):
        proposed_loc = coord_add(self._robot, instruction)
        if proposed_loc not in self._boxes and proposed_loc not in self._walls:
            # way is clear
            self._robot = proposed_loc
        if proposed_loc in self._walls:
            # can't move
            return
        elif proposed_loc in self._boxes:
            # track the first box
            move_to = proposed_loc
            # move pointer until free space or wall
            while move_to in self._boxes:
                move_to = coord_add(move_to,instruction)
            # make a decision
            if move_to in self._walls:
                # can't move
                return
            # move the boxes... which just means moving one box...
            # remove box at to_move, add box at proposed_loc
            self._boxes.remove(proposed_loc)
            self._boxes.add(move_to)
            # move the robot
            self._robot = proposed_loc

    @property
    def gps_sum(self):
        ret = 0
        for box in self._boxes:
            ret += box[0] + box[1]*100
        return ret

    def __repr__(self):
        ret = ''
        for j in range(0,self._bounds[0]):
            for i in range(0, self._bounds[1]):
                if (i,j) in self._boxes:
                    ret += 'O'
                elif (i,j) in self._walls:
                    ret += '#'
                elif (i,j) == self._robot:
                    ret += '@'
                else:
                    ret += '.'
            ret += '\n'
        return ret

def coord_add(coord1, coord2):
    return (coord1[0]+coord2[0], coord1[1]+coord2[1])

def part1(parsed):
    # print(parsed)
    warehouse, _, moves = parsed
    for move in moves:
        warehouse.move_robot(move)
    return warehouse.gps_sum

def part2(parsed):
    _, warehouse, moves = parsed
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