import pathlib
import sys

SAMPLE_ANSWER_1 = 1588
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    template, rules = puzzle_input.split('\n\n')
    rules = [r for r in rules.splitlines()]
    rules_dict = {}
    for rule in rules:
        p, i = rule.split(' -> ')
        rules_dict.update({p:i})
    return template, rules_dict

def step(start, rules):
    pass

def part1(parsed):
    template = parsed[0]
    
    return 0

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