import pathlib
import sys

SAMPLE_ANSWER_1 = 26
SAMPLE_ANSWER_2 = 61229

SEGMENTS_PER_DIGIT = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

def parse(puzzle_input):
    # parse the input
    return [line.split(' | ') for line in puzzle_input.split('\n')]

# unique digits are 1, 4, 7, 8
# # using segments len 2, 4, 3, 7
def unique_identifier(s):
    switch = {2:1, 4:4, 3:7, 7:8}
    return switch.get(len(s), False)

def part1(parsed):
    ret = 0
    for p in parsed:        
        ret += len([display for display in p[1].split(' ') if unique_identifier(display)])
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