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
    ret = start[0]
    
    for i in range(0, len(start)-1):
        ret += rules.get(start[i:i+2], '')
        ret += start[i+1]

    return ret

def most_minus_less(template):
    min = len(template)
    max = 0
    for c in set(template.split()):
        temp = template.count(c)
        if temp > max:
            max = temp
        if temp < min:
            min = temp
    return max - min

def part1(parsed):
    template, rules = parsed
    for i in range(0, 10):
        # print(template)
        # print( '-------------')
        template = step(template, rules)
    return most_minus_less(template)

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