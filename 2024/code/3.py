import pathlib
import re
import sys

SAMPLE_ANSWER_1 = 161
SAMPLE_ANSWER_2 = 48

def parse(puzzle_input):
    # parse the input
    return re.findall("mul\(\d{1,4},\d{1,4}\)|don't\(\)|do\(\)",puzzle_input)
    
def mul(match):
    x, y = map(int,(re.findall("\d{1,4}", match)))
    return x*y

def part1(parsed):
    # print(parsed)
    ret = 0
    for m in parsed:
        if m != 'do()' and m != "don't()":
            ret += mul(m)
    return ret

def part2(parsed):
    # print(parsed)
    enabled = True
    ret = 0
    for p in parsed:
        if p == "don't()":
            enabled = False
        elif p == "do()":
            enabled = True
        else:
            if enabled:
                ret += mul(p)
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
