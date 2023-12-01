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
        # {(r, c): n}
        self._spaces = {}
        self._called = set()
        self._round = 0
        rows = [[s for s in re.findall(r'([0-9]+)[ ]?', r)] for r in input.split('\n')]
        for r in range(5):
            for c in range(5):
                self._spaces[(r, c)] = int(rows[r][c])
                
    def print(self):
        pr = ''
        for r in range(5):
            for c in range(5):
                p = self._spaces.get((r, c))
                if p in self._called:
                    pr += f'!{p}!'
                else:
                    print(f'{[p]} is not in {self._called}')
                    pr += str(p)
                pr += ' '
            pr += '\n'
        print(pr)

    def call(self, called):
        self._called.add(called)
        self._round += 1
        return (self._round, self._called)
    
    def is_winning(self):
        #check rows
        for r in range(5):
            if self._spaces.get((r, 0)) in self._called and self._spaces.get((r, 1)) in self._called and self._spaces.get((r, 2)) in self._called and self._spaces.get((r, 3)) in self._called and self._spaces.get((r, 4)) in self._called:
                return True
        #check columns
        for c in range(5):
            if self._spaces.get((0, c)) in self._called and self._spaces.get((1, c)) in self._called and self._spaces.get((2, c)) in self._called and self._spaces.get((3, c)) in self._called and self._spaces.get((4, c)) in self._called:
                return True
        return False

    def score(self):
        unmarked = 0
        for r in range(5):
            for c in range(5):
                val = self._spaces.get((r, c))
                if val not in self._called:
                    unmarked += val
        return unmarked * self._round

        
class BingoCompetition():
    def __init__(self, calls, boards):
        self._calls = calls
        self._boards = boards
    
    def run(self):
        bingo = False
        index = 0
        while not bingo:
            for board in self._boards:
                board.call(self._calls[index])
                if board.is_winning():
                    return board.score()
            index += 1

def part1(calls_and_boards):
    calls, boards = calls_and_boards
    our_competition = BingoCompetition(calls, boards)
    return our_competition.run()

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