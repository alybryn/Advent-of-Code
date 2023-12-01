import pathlib
import re
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

DIGIT_STRINGS = ['0','1','2','3','4','5','6','7','8','9']

def parse(puzzle_input):
    # parse the input
    return [line for line in puzzle_input.split()]

def get_digits(r, s):
    return re.findall(r, s)
    # return [d for d in s if d in DIGIT_STRINGS]

def get_digits2(r, s):
    return re.match(r, s).groupdict()

# def findall_digits(s):
#     return re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', s)

def s_to_n(s):
    switch={
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    if s in DIGIT_STRINGS:
        return s
    return switch.get(s)

def part1(parsed):
    ret = 0
    for line in parsed:
        # should still use findall?
        digits = get_digits(r'\d', line)
        ret += int(digits[0] + digits[-1])
    return ret

def part2(parsed):
    ret = 0
    i = 0
    for line in parsed:
        digits = get_digits(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
        back_digits = get_digits(r'\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', line[::-1])
        digit1 = get_digits2(r'^(.*?)(one|two|three|four|five|six|seven|eight|nine|\d)', line)
        # if digit1 != digits[0]:
        #     print(f"1: {digit1} != {digits[0]}")
        digit2 = get_digits2(r'(.*)(?P<d>one|two|three|four|five|six|seven|eight|nine|\d)(.*?$)', line)
        if digit2.get('d') != back_digits[0][::-1]:
            print(f"2: {digit2} != {back_digits[0][::-1]}")
        # if (digits[-1] != back_digits[0][::-1]):
        #     print('________')
        #     print(line)
        #     print(digits)
        #     print([s[::-1] for s in back_digits])
        #     print('________')
        # if line == 'sgeightwo3':
        #     print(digits)
        #     print(back_digits[1][::-1])
        #print("-----" + line + " " + s_to_n(digits[0]) + s_to_n(back_digits[0][::-1]))
        ret += int(s_to_n(digits[0]) + s_to_n(back_digits[0][::-1]))
    return ret

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