import pathlib
import sys

SAMPLE_ANSWER_1 = 8
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input

neighbors_matrix = {'F': ([(0,-1),( 1,0)]),
                    'L': ([(0, 1),( 1,0)]),
                    'J': ([(0, 1),(-1,0)]), 
                    '7': ([(0,-1),(-1,0)]),
                    'S': ([(0,-1),(0, 1),(-1,0),( 1,0)]),
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
        return [(self._loc[0] + using[0][0], self._loc[1] + using[0][1]), (self._loc[0] + using[1][0], self._loc[1] + using[1][1])] 

    def set_neighbors(self, new_neighbors):
        self._neighbors = new_neighbors

    def __str__(self) -> str:
        return self._type

def part1(parsed):
    return 0

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