import pathlib
import sys

SAMPLE_ANSWER_1 = 136
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return Platform([list(line) for line in puzzle_input.split()])

class Platform():
    def __init__(self, input) -> None:
        self._southern_edge = len(input)
        self._eastern_edge = len(input[0])
        self._map = {}
        for x in range(self._southern_edge):
            for y in range(self._eastern_edge):
                if input[x][y] != '.':
                    # round is True, square is False, none is None
                    self._map.update({(x,y): input[x][y] == 'O'})


def part1(parsed):
    return parsed

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