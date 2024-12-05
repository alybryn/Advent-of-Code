import pathlib
import sys

SAMPLE_ANSWER_1 = 143
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    rules, updates = puzzle_input.split("\n\n")
    rules = [Rule(r) for r in rules.split("\n")]
    updates = [u for u in updates.split("\n")]
    return rules, updates

class Rule:
    def __init__(self, r):
        self.before, self.after = r.split("|")

    def isBroken(self, u):
        b = u.find(self.before)
        a = u.find(self.after)
        if a == -1 or b == -1:
            return False
        return b > a

def middle(update):
    l=[u for u in update.split(",")]
    return int(l[len(l)/2])

def part1(parsed):
    print(parsed)
    rules, updates = parsed
    s = 0
    for update in updates:
        breaks = False
        for rule in rules:
            if rule.isBroken(update):
                breaks = True
        if not breaks:
            s += middle(update)
    return s

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
