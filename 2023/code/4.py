import pathlib
import re
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

wins_per_card = {}
number_of_cards = {}

def parse(puzzle_input):
    # parse the input
    wins = {}
    haves = {}
    for line in puzzle_input.split('\n'):
        card_number, winning_and_having = re.split(r':\s+', line)
        card_number = int(re.split(r'\s+', card_number)[1])
        # card_number = int(card_number.split(' ')[1])
        # print(card_number)
        winning, having = re.split(r'\s+\|\s+', winning_and_having)
        wins.update({card_number: [int(w) for w in re.split(r'\s+', winning)]})
        haves.update({card_number: [int(h) for h in re.split(r'\s+', having)]})
    return wins, haves

def score_card(win, have):
    score = 0
    matches = 0
    for w in win:
        if w in have:
            matches += 1
            if score == 0:
                score = 1
            else:
                score = score * 2
    # print(score)
    return score, matches

def part1(parsed):
    winning, having = parsed[0], parsed[1]
    score = 0
    for k in winning.keys():
        s, m = score_card(winning.get(k), having.get(k))
        wins_per_card.update({k: m})
        number_of_cards.update({k: 1})
        score += s
    return score

def part2(parsed):
    total = 0
    # print(wins_per_card)
    # print(number_of_cards)
    for k in wins_per_card.keys():
        # add this card's number to total
        add = number_of_cards.get(k)
        total += add
        # increase count of next .get(k) cards
        # BY HOW MANY OF THIS CARD
        increase = wins_per_card.get(k)
        for i in range(k, k + increase):
            # adjust up
            number_of_cards.update({i+1: number_of_cards.get(i+1) + add})
    # print(number_of_cards)
    return total

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