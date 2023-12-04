import pathlib
import re
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

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

def score_1(win, have):
    score = 0
    for w in win:
        if w in have:
            if score == 0:
                score = 1
            else:
                score = score * 2
    # print(score)
    return score

def part1(parsed):
    winning, having = parsed[0], parsed[1]
    score = 0
    for k in winning.keys():
        score += score_1(winning.get(k), having.get(k))
    return score

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