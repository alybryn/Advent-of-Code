import pathlib
import re
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

DIGIT_STRINGS = ['0','1','2','3','4','5','6','7','8','9']

def parse(puzzle_input):
    # parse the input
    return [line for line in puzzle_input.split()]

def get_digits(s):
    return [d for d in s if d in DIGIT_STRINGS]

def findall_digits(s):
    return re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', s)

def part1(parsed):
    ret = 0
    for line in parsed:
        digits = get_digits(line)
        ret += int(digits[0] + digits[-1])
    return ret

def part2(parsed):
    print('part 2')
    ret = 0
    for line in parsed:
        digits = findall_digits(line)
        print(digits)#[0] + digits[-1])
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