import pathlib
import re
import sys

SAMPLE_ANSWER_1 = 161
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return re.findall("mul\(\d{1,4},\d{1,4}\)",puzzle_input)

def mul(match):
    x, y = map(int,(re.findall("\d{1,4}", match)))
    return x*y

def part1(parsed):
    parsed = parsed[0]
    # print(parsed)
    ret = 0
    for m in parsed:
        ret += mul(m)
    return ret

def part2(parsed):
    parsed = parsed[1]
    print(parsed)
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
