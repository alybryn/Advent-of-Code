import pathlib
import sys

SAMPLE_ANSWER_1 = 26397
SAMPLE_ANSWER_2 = 288957

illegal_char_scores = {')':3, ']':57, '}':1197, '>': 25137}
autocomplete_char_scores = {')':1, ']':2, '}':3, '>': 4}

part1_ans = []
part2_ans = []

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
            # print(expectations)
        # think about checking empty expections here #
        elif line[i] == expectations[-1]:
            expectations.pop()
        # case line[i] is not expected, return char
        else:
            part1_ans.append(line[i])
            return
    # case unfulfilled expections remain
    if len(expectations) != 0:
        part2_ans.append(expectations[::-1])
        return

def loop(parsed):
    for line in parsed:
        scan_line(line)

def part1(parsed):
    score = 0
    for ans in part1_ans:
        score += illegal_char_scores.get(ans, 0)
    return score

def part2(parsed):
    scores = []
    for ans in part2_ans:
        this_score = 0
        for char in ans:
            this_score = this_score * 5
            this_score = this_score + autocomplete_char_scores.get(char)
        scores.append(this_score)
    i = len(scores) // 2
    return sorted(scores)[i]

def solve(puzzle_input):
    data = parse(puzzle_input)
    loop(data)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}")
        puzzle_input = pathlib.Path(path).read_text().strip()

        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))