from enum import Enum
import pathlib
import sys

SAMPLE_ANSWER_1 = 6440
SAMPLE_ANSWER_2 = 5905


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

card_list = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

class Hand:
    def __init__(self, cards, bet) -> None:
        self._cards = cards
        counts = []
        for card in card_list:
            counts.append(self._cards.count(card))
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
        return f"Hand with:\n\tCards: {self._cards}\n\tType: {self._type}\n\tBet: {self._bet}"
    
    @property
    def input(self):
        return {'cards': self._cards, 'bet': self._bet}

class Hand2:
    def __init__(self, hand) -> None:
        input = hand.input
        self._cards = input.get('cards')
        counts = []
        jokers = self._cards.count('J')
        for k in card_list:
            if k != 'J':
                counts.append(self._cards.count(k))
        temp_type = None
        if 5 in counts:
            temp_type = HandType.FIVE
        elif 4 in counts:
            temp_type = HandType.FOUR
        elif 3 in counts and 2 in counts:
            temp_type = HandType.FULL
        elif 3 in counts:
            temp_type = HandType.THREE
        elif counts.count(2) == 2:
            temp_type = HandType.TWO
        elif 2 in counts:
            temp_type = HandType.ONE
        else:
            temp_type = HandType.HIGH
        
        # round 2: (make sure to assign in all cases)
        if jokers == 0:
            self._type = temp_type
        elif jokers == 5:
            self._type = HandType.FIVE
        elif temp_type == HandType.FOUR: # jokers = 1
            self._type = HandType.FIVE
        elif temp_type == HandType.THREE: # jokers = 1, 2
            if jokers == 1:
                self._type = HandType.FOUR
            else: # jokers == 2
                self._type = HandType.FIVE
        elif temp_type == HandType.TWO: # jokers = 1
            self._type = HandType.THREE
        elif temp_type == HandType.ONE: # jokers = 1, 2, 3
            if jokers == 1:
                self._type = HandType.THREE
            elif jokers == 2:
                self._type = HandType.FOUR
            else: # jokers == 3
                self._type = HandType.FIVE
        else: #temp_type == HIGH, jokers = 1, 2, 3, 4
            if jokers == 1:
                self._type = HandType.ONE
            elif jokers == 2:
                self._type = HandType.THREE
            elif jokers == 3:
                self._type = HandType.FOUR
            else: # jokers = 4
                self._type = HandType.FIVE

        self._bet = input.get('bet')

    def __gt__(self, other):
        if self._type != other._type:
            return self._type > other._type
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
            "J": 1,
            "Q": 12,
            "K": 13,
            "A": 14
        }
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
        return f"Hand with:\n\tCards: {self._cards}\n\tType: {self._type}\n\tBet: {self._bet}"


def part1(parsed):
    
    rank = 1
    table = 0
    for hand in sorted(parsed):
        table += (hand.winnings(rank))
        rank += 1
    return(table)

def part2(parsed):
    for hand in [Hand2(hand) for hand in parsed]:
        print(hand)
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