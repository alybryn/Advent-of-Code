import pathlib
import sys

SAMPLE_ANSWER_1 = 8
SAMPLE_ANSWER_2 = 10

def parse(puzzle_input):
    # parse the input
    lines = [[c for c in list(lines)] for lines in puzzle_input.split()]
    pipe_map = {}
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            type = lines[r][c]
            pipe_map.update({(c,r): Pipe((c,r), type)})
            if type == 'S':
                pipe_map.update({'S': (c,r)})
    return pipe_map

neighbors_matrix = {'F': ([(0, 1),( 1,0)]),
                    'L': ([(0,-1),( 1,0)]),
                    'J': ([(0,-1),(-1,0)]), 
                    '7': ([(0, 1),(-1,0)]),
                    '|': ([(0,-1),( 0,1)]),
                    '-': ([(1, 0),(-1,0)]),
                    'S': ([(0,-1),(0, 1),(-1,0),( 1,0)]),
                    '.': (),
                    }

class Pipe():
    def __init__(self, loc, type) -> None:
        self._type = type
        self._loc = loc
        self._neighbors = []

    def potential_neighbors(self):
        using = neighbors_matrix.get(self._type)
        ret = []
        for matrix in using:
            ret.append((self._loc[0] + matrix[0], self._loc[1] + matrix[1]))
        return ret


    def set_neighbors(self, new_neighbors):
        self._neighbors = new_neighbors

    def __str__(self) -> str:
        return self._type

def link_back(pipe, pipe_map, prev=[]):
    ret = []
    # print(f'Finding a link for {pipe_map.get(pipe)}')
    for index in pipe_map.get(pipe).potential_neighbors():
        if index in prev:
            # print(f'already been to {index}')
            continue
        indexed = pipe_map.get(index)
        if indexed:
            # print(indexed.potential_neighbors())
            if pipe in indexed.potential_neighbors():
                ret.append(index)
    # print(ret)
    return ret

def part1(pipe_map):
    start_index = pipe_map.get('S')
    s_connects = link_back(start_index, pipe_map)
    path_taken = set()
    path_taken.add(start_index)
    branch_0 = s_connects[0]
    branch_1 = s_connects[1]
    # print(f'Setting out from {branch_0} and {branch_1}')
    count = 1
    while(branch_0 != branch_1):
        path_taken.add(branch_0)
        path_taken.add(branch_1)
        branch_0 = link_back(branch_0, pipe_map, path_taken)[0]
        branch_1 = link_back(branch_1, pipe_map, path_taken)[0]
        count += 1
    return count

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