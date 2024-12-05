import pathlib
import sys

SAMPLE_ANSWER_1 = 143
SAMPLE_ANSWER_2 = 123

def parse(puzzle_input):
    # parse the input
    rules, updates = puzzle_input.split("\n\n")
    rules = make_rules(rules)
    updates = [[u for u in update.split(",")] for update in updates.split("\n")]
    good_updates = [update for update in updates if check(update, rules)]
    bad_updates = [update for update in updates if not check(update, rules)]
    return good_updates, bad_updates, rules

def make_rules(rules):
    d = {}
    for r in rules.split("\n"):
        b,a = r.split('|')
        t = d.get(a,set())
        t.add(b)
        d.update({a:t})
    return d

def check(update, rules):
    for i in range(0, len(update)):
        if len(rules.get(update[i],set()).intersection(update[i:])) > 0:
            return False
    return True

def middle(update):
    return int(update[len(update)//2])

def fix(update, rules):
    for i in range(0, len(update)):
        problems = rules.get(update[i],set()).intersection(update[i:])
        if len(problems) > 0:
            update = move(update, i, problems)
            return update

def move(update, index, problems):
    # find the index for insertion
    maxI = 0
    for i in range(len(update)):
        if update[i] in problems:
            maxI = i
    t = update.pop(index)
    update.insert(maxI,t)
    return update

def part1(parsed):
    # print(parsed)
    good_updates = parsed[0]
    s = 0
    for update in good_updates:
        s += middle(update)
    return s

def part2(parsed):
    _, bad_updates, rules = parsed
    s = 0
    for update in bad_updates:
        while not check(update, rules):
            update = fix(update, rules)
        s += middle(update)
    return s

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
