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

def adding(point, vector):
    return (point[0] + vector[0], point[1] + vector[1])

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
            ret.append(adding(pipe, matrix))
        return ret
    
    def change_start_type(self):
        potentates = self.potential_neighbors(self._start)
        correct = []
        for index in potentates:
            if self._start in self.potential_neighbors(index):
                correct.append(index)
        for k in ['F','L','J','7','|','-']:
            start_neighbors_check = []
            for matrix in neighbors_matrix.get(k):
                start_neighbors_check.append(adding(self._start, matrix))
            if start_neighbors_check == correct:
                self._locs.update({self._start: k})
                return

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

    def count_inside(self):
        c = 0
        for k in self._locs.keys():
            if k not in self._loop:
                if self.count(k):
                    c += 1
        return c

    def count(self, loc):
        # print(f'checking: {self._locs[loc]}')
        inside = False
        lookup = {('F','7'):0,('F','J'):1,('L','7'):1,('L','J'):0}
        y = loc[1]
        mem = None
        for x in range(0, loc[0]):
            if (x, y) in self._loop:
                type = self._locs.get((x,y))
                # print(type)
                if type in ['F', 'L']:
                    mem = type
                elif type in ['7','J']:
                    if lookup.get((mem, type)):
                        inside = not inside
                elif type == '|':
                    inside = not inside
        return 1 if inside else 0

    @property
    def half_loop_len(self):
        return len(self._loop) // 2

def part1(pipe_map):
    return pipe_map.half_loop_len

def part2(pipe_map):
    pipe_map.change_start_type
    # print(pipe_map.count((14, 3)))
    return pipe_map.count_inside()

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