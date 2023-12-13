import pathlib
import sys

SAMPLE_ANSWER_1 = 405
SAMPLE_ANSWER_2 = None

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

def find_inflection(pattern):
    for i in range(1, len(pattern)):
        # pass sides to helper
        # print(f'{pattern[:i][::-1]} v {pattern[i:]}')
        if is_mirror(pattern[:i][::-1], pattern[i:]):
            return i

# arg: pattern: string of single pattern
# returns list of strings arranged as they were vertically
def vertical(pattern):
    # return [list(f) for f in zip(*[list(c) for c in pattern.split('\n')])]
    return [''.join(list(f)) for f in zip(*[list(c) for c in pattern.split('\n')])]

# arg: pattern: string of single pattern
def horizontal(pattern):
    return pattern.split('\n')

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