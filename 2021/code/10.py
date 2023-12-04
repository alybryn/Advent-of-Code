import pathlib
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

char_scores = {')':3, ']':57, '}':1197, '>': 25137}

def parse(puzzle_input):
    # parse the input
    return [line for line in puzzle_input.split()]

def find_corrupted_value(chunk, expectation):
    found = '}'
    return f'Expected {expectation} but found {found} instead'

# def scan_line(line):
#     bad = 0
#     for i in range(len(line)):
#         print((line[i+1:], line[i]))
#     return char_scores.get(line[bad], 0)

def scan_line(line):
    expectations = []
    pairs = {'(':')', '[':']', '{':'}', '<':'>'}
    for i in range(len(line)):
        if line[i] in ['(', '[', '{', '<']:
            # creates an expection
            expectations.append(pairs.get(line[i]))
        # think about checking empty expections here #
        elif line[i] == expectations[-1]:
            expectations.pop()
        # case line[i] is not expected, return char
        else:
            return line[i]
    # case unfulfilled expections remain
    if len(expectations) != 0:
        return str(expectations)
    
def part1(parsed):
    score = 0
    for line in parsed:
        score += char_scores.get(scan_line(line), 0)
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