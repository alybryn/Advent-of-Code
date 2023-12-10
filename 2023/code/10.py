import pathlib
import sys

SAMPLE_ANSWER_1 = 8
SAMPLE_ANSWER_2 = 10

def parse(puzzle_input):
    # parse the input
    lines = [[c for c in list(lines)] for lines in puzzle_input.split()]
    pipe_map = PipeMap(lines)
    pipe_map.pipe_loop()
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

class PipeMap():
    # input is [[c,...],[c,...],...]
    def __init__(self, input) -> None:
        self._locs = {}
        self._start = None
        for r in range(len(input)):
            for c in range(len(input[0])):
                type = input[r][c]
                self._locs.update({(c,r): type})
                if type == 'S':
                    self._start = (c,r)

        self._loop = {self._start}

    def potential_neighbors(self, pipe):
        type = self._locs.get(pipe)
        if type == None:
            return []
        using = neighbors_matrix.get(type)
        ret = []
        for matrix in using:
            ret.append((pipe[0] + matrix[0], pipe[1] + matrix[1]))
        return ret
    
    def link_back(self, pipe, prev=[]):
        for index in self.potential_neighbors(pipe):
            if index in prev:
                continue
            if pipe in self.potential_neighbors(index):
                return index

    def pipe_loop(self) -> None:
        # start at start
        next = self.link_back(self._start, self._loop)
        # while link back not empty
        while next:
            # append and continue
            self._loop.add(next)
            next = self.link_back(next, self._loop)

    @property
    def half_loop_len(self):
        return len(self._loop) // 2

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