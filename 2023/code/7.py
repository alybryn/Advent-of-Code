from enum import Enum
import pathlib
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None


def parse(puzzle_input):
    # parse the input
    return [
        Hand(l[0], int(l[1]))
        for l in [line.split() for line in puzzle_input.split("\n")]
    ]

class HandType(int, Enum):
    FIVE = 6
    FOUR = 5
    FULL = 4
    THREE = 3
    TWO = 2
    ONE = 1
    HIGH = 0

card_values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

class Hand:
    def __init__(self, cards, bet) -> None:
        self._cards = cards
        counts = []
        for k in card_values.keys():
            counts.append(self._cards.count(k))
        if 5 in counts:
            self._type = HandType.FIVE
        elif 4 in counts:
            self._type = HandType.FOUR
        elif 3 in counts and 2 in counts:
            self._type = HandType.FULL
        elif 3 in counts:
            self._type = HandType.THREE
        elif counts.count(2) == 2:
            self._type = HandType.TWO
        elif 2 in counts:
            self._type = HandType.ONE
        else:
            self._type = HandType.HIGH
        self._bet = bet

    def __gt__(self, other):
        if self._type != other._type:
            return self._type > other._type
        for i in range(5):
            s = card_values.get(self._cards[i])
            o = card_values.get(other._cards[i])
            if s != o:
                return s > o
        print('unreachable line, Hand.__gt__')
        return None

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