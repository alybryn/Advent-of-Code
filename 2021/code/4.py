import pathlib
import sys

SAMPLE_ANSWER_1 = 4512
SAMPLE_ANSWER_2 = 1924

def parse(puzzle_input):
    # parse the input
    calls, *rem = puzzle_input.split('\n\n')
    calls = [int(c) for c in calls.split(',')]
    boards = []
    for section in rem:
        boards.append(BingoBoard(section))
    return (calls, boards)

class BingoSpace():
    def __init__(self, row, col):
        self._row = row
        self._col = col
        self._marked = False
    
    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col

    @property
    def marked(self):
        return self._marked

    def mark(self):
        self.marked = True

class BingoBoard():
    def __init__(self, input):
        self._spaces = {}
        rows = [[s for s in r.split] for r in input]
        for r in range(5):
            for c in range(5):
                self._spaces.add(BingoSpace(r, c, rows[r][c]))

    def print(self):
        pr = ''
        for r in range(5):
            for c in range(5):
                pr += self._spaces.
        
class BingoCompetition():
    def __init__(self, calls, boards):
        self._calls = calls
        self._boards = boards

def part1(calls_and_boards):
    calls, boards = calls_and_boards
    print(calls)
    return 0

def part2(calls_and_boards):
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