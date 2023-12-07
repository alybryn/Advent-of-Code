from enum import Enum
import pathlib
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return [[Hand(l[0], int(l[1])) for l in line.split()] for line in puzzle_input.split('\n')]

class HandType(int, Enum):
    FIVE = 6
    FOUR = 5
    FULL = 4
    THREE = 3
    TWO = 2
    ONE = 1
    HIGH = 0

class Hand():
    def __init__(self, cards, bet) -> None:
        self._cards = cards
        self._type = HandType.FIVE
        self._bet = bet

    def __gt__(self, other):
        # TODO
        return True
    
    def winnings(self, rank):
        return self._bet * rank
    
    def __str__(self) -> str:
        return f'Hand with:\n\tCards: {self._cards}\n\tType: {self._type}\n\tBet: {self._bet}'
        

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