import pathlib
import sys

SAMPLE_ANSWER_1 = 405
SAMPLE_ANSWER_2 = 400

def parse(puzzle_input):
    # parse the input
    patterns = [line for line in puzzle_input.split('\n\n')]
    return patterns
    # patterns_flipped = []
    # for pattern in patterns:
    #     patterns_flipped.append([''.join(list(f)) for f in zip(*[list(c) for c in pattern.split('\n')])])
    # return [pattern.split('\n') for pattern in patterns], patterns_flipped

def is_mirror(side1, side2):
    for i in range(min(len(side1), len(side2))):
        # print(f'{side1[i]} v {side2[i]}')
        if side1[i] != side2[i]:
            return False
    return True

# orientation agnostic
def find_inflection(pattern):
    for i in range(1, len(pattern)):
        # pass sides to helper
        if is_mirror(pattern[:i][::-1], pattern[i:]):
            return i

# arg: pattern: string of single pattern
# arg: disallowed: optional int of previous reflection line
# return: unmodified n, 'h'|'v'
def check_inflection(pattern, disallowed=None):
    n = (find_inflection(vertical(pattern)), 'v')
    if n[0] and n != disallowed:
        return n
    n = (find_inflection(horizontal(pattern)), 'h')
    if n[0] and n != disallowed:
        return n

# arg: pattern: string of single pattern
# returns list of strings arranged as they were vertically
def vertical(pattern):
    # return [list(f) for f in zip(*[list(c) for c in pattern.split('\n')])]
    return [''.join(list(f)) for f in zip(*[list(c) for c in pattern.split('\n')])]

# arg: pattern: string of single pattern
def horizontal(pattern):
    return pattern.split('\n')

# arg: pattern: string of single pattern (incl. \n)
# arg: disallowed: int of previous reflection
def fix_smudge(pattern, disallowed):
    patt_list = list(pattern)
    for i in range(len(patt_list)):
        if patt_list[i] == '\n':
            # print(i)
            # print(''.join(patt_list[i:]))
            continue
        new_str = ''
        if patt_list[i] == '#':
            new_pattern = patt_list.copy()
            new_pattern[i] = '.'
            # new_str = ''.join(new_pattern)
        else: # if patt_list[i] == '.':
            new_pattern = patt_list.copy()
            new_pattern[i] = '#'
        new_str = ''.join(new_pattern)
        n = check_inflection(new_str, disallowed)
        if n and n != disallowed:
            return n
        if i == 120:
            print(new_str)

def value(inflection):
    return inflection[0] if inflection[1] == 'v' else inflection[0] * 100

def part1(parsed):

    ret = 0

    for pattern in parsed:
        n = find_inflection(horizontal(pattern))
        if n:
            ret += n * 100
            continue
        ret += find_inflection(vertical(pattern))
    return ret

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