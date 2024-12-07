from collections import namedtuple
import pathlib
import sys

SAMPLE_ANSWER_1 = 3749
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    ret = []
    for line in puzzle_input.splitlines():
        result, values = line.split(": ")
        values = [int(value) for value in values.split(" ")]
        # result = int(result)
        # first = values[0]
        # values = values[1:]
        ret.append(Test(result=int(result), first=values[0], values=values[1:]))
    return ret

Test = namedtuple('Test', ['result', 'first', 'values'])

def attempt_add_mult(test):
    if len(test.values) == 0:
        return test.result == test.values[0]

# def attempt(result, values):
#     if len(values) == 1:
#         return result == values[0]
#     return attempt(result, [values[0] + values[1]] + values[2:]) or attempt(result, [values[0] * values[1]] + values[2:])

def part1(parsed):
    # print(parsed)
    ret = 0
    for test in parsed:
        if attempt_add_mult(test):
            ret += test.result
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
