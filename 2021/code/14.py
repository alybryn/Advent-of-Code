import pathlib
import sys

SAMPLE_ANSWER_1 = 1588
SAMPLE_ANSWER_2 = 2188189693529

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
    for c in set(list(template)):
        temp = template.count(c)
        if temp > max:
            max = temp
        if temp < min:
            min = temp
    return max - min

def polymerize(rules, start, rep):
    ret = {}
    for i in range(0,len(start)-1):
        print(f'counting: {start[i]}{start[i+1]}')
        ret = dict_combine(ret, count_letters(rules, start[i], start[i+1],rep))
        print(ret)
    return most_minus_least(ret)

def count_letters(rules, a, b, rep):
    if rep == 0:
        if a == b:
            return {a:2}
        return {a:1, b:1}
    c = rules.get(f'{a}{b}')
    if not c:
        if a == b:
            return {a:2}
        return {a:1, b:1}
    return dict_combine(count_letters(rules,a,c,rep-1),count_letters(rules,c,b,rep-1))

def dict_combine(a, b):
    keys = set(a.keys()).union(b.keys())
    ret = {}
    for key in keys:
        ret.update({key: a.get(key,0) + b.get(key,0)})
    return ret

def most_minus_least(letter_dict):
    return max(letter_dict.values()) - min(letter_dict.values())

def part1(parsed):
    template, rules = parsed
    return polymerize(rules, template, 0)
    for i in range(0, 10):
        # print(template)
        # print( '-------------')
        template = step(template, rules)
    return most_minus_less(template)

def part2(parsed):
    # template, rules = parsed
    # for i in range(0, 40):
    #     template = step(template, rules)
    # return most_minus_less(template)
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