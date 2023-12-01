import pathlib
import re
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

class BingoBoard():
    def __init__(self, input):
        # {(r, c): (n, marked)}
        self._spaces = {}
        rows = [[s for s in re.findall(r'([0-9]+)[ ]?', r)] for r in input.split('\n')]
        #rows = [r for r in input.split('\n')]
        #print(rows)
        for r in range(5):
            for c in range(5):
                self._spaces[(r, c)] = (rows[r][c], False)
                #self._spaces.update({(r, c): (rows[r][c], False)})

    def print(self):
        pr = ''
        for r in range(5):
            for c in range(5):
                pr += self._spaces.get((r, c))[0]
                pr += ' '
            pr += '\n'
        print(pr)
        
class BingoCompetition():
    def __init__(self, calls, boards):
        self._calls = calls
        self._boards = boards

def part1(calls_and_boards):
    calls, boards = calls_and_boards
    boards[0].print()
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