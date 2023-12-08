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
    FIVE_KIND = 6
    FOUR_KIND = 5
    FULL_HOUSE = 4
    THREE_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0

card_list = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

class Hand:
    def __init__(self, cards, bet) -> None:
        self._cards = cards
        counts = []
        for card in card_list:
            counts.append(self._cards.count(card))
        if 5 in counts:
            self._type = HandType.FIVE_KIND
        elif 4 in counts:
            self._type = HandType.FOUR_KIND
        elif 3 in counts and 2 in counts:
            self._type = HandType.FULL_HOUSE
        elif 3 in counts:
            self._type = HandType.THREE_KIND
        elif counts.count(2) == 2:
            self._type = HandType.TWO_PAIR
        elif 2 in counts:
            self._type = HandType.ONE_PAIR
        else:
            self._type = HandType.HIGH_CARD
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
            temp_type = HandType.FIVE_KIND
        elif 4 in counts:
            temp_type = HandType.FOUR_KIND
        elif 3 in counts and 2 in counts:
            temp_type = HandType.FULL_HOUSE
        elif 3 in counts:
            temp_type = HandType.THREE_KIND
        elif counts.count(2) == 2:
            temp_type = HandType.TWO_PAIR
        elif 2 in counts:
            temp_type = HandType.ONE_PAIR
        else:
            temp_type = HandType.HIGH_CARD
        # if jokers != 0:
            # print(f'temp_type: {temp_type.name}, jokers = {jokers}')

        # round 2: (make sure to assign in all cases)
        if jokers == 0:
            self._type = temp_type
        elif jokers == 5:
            self._type = HandType.FIVE_KIND
        elif temp_type == HandType.FOUR_KIND: # jokers = 1
            self._type = HandType.FIVE_KIND
        elif temp_type == HandType.THREE_KIND: # jokers = 1, 2
            if jokers == 1:
                self._type = HandType.FOUR_KIND
            else: # jokers == 2
                self._type = HandType.FIVE_KIND
        elif temp_type == HandType.TWO_PAIR: # jokers = 1
            self._type = HandType.FULL_HOUSE
        elif temp_type == HandType.ONE_PAIR: # jokers = 1, 2, 3
            if jokers == 1:
                self._type = HandType.THREE_KIND
            elif jokers == 2:
                self._type = HandType.FOUR_KIND
            else: # jokers == 3
                self._type = HandType.FIVE_KIND
        else: #temp_type == HIGH, jokers = 1, 2, 3, 4
            if jokers == 1:
                self._type = HandType.ONE_PAIR
            elif jokers == 2:
                self._type = HandType.THREE_KIND
            elif jokers == 3:
                self._type = HandType.FOUR_KIND
            else: # jokers = 4
                self._type = HandType.FIVE_KIND

        # print(self._type.name)
        self._bet = input.get('bet')

    def __gt__(self, other):
        if self._type != other._type:
        #     if self._type > other._type:
        #         print(f'{self._type.name} gt {other._type.name}')
        #         return True
        #     else:
        #         print(f'{other._type.name} gt {self._type.name}')
        #         return False
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
                # if 2 in [s, o]:
                #     print(f'{self._cards[i]} {">" if s>o else "<"} {other._cards[i]}')
                return s > o
        print('unreachable line, Hand.__gt__')
        return None

    def winnings(self, rank):
        # print(f'multiplying {self._bet} and {rank}')
        return self._bet * rank
    
    @property
    def has_joker(self):
        return 'J' in self._cards

    def __str__(self) -> str:
        return f"Hand2 with:\n\tCards: {self._cards}\n\tType: {self._type.name}\n\tBet: {self._bet}"

def get_table_winnings(hands):
    rank = 0
    table = 0
    for hand in sorted(hands):
        rank += 1
        # print(hand)
        table += hand.winnings(rank)
        # print(f'table becomes {table}')
    assert(rank == len(hands))
    return table

def part1(parsed):
    return get_table_winnings(parsed)

def part2(parsed):
    # hands = []
    # for hand in parsed:
    #     new_hand = Hand2(hand)
    #     if new_hand.has_joker:
    #         print(new_hand)
        # hands.append(new_hand)
    # for hand in sorted(hands):
        # if hand.has_joker:
            # print(hand)
    return get_table_winnings([Hand2(hand) for hand in parsed])

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
