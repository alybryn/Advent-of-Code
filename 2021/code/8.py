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

def minus(big, small):
    ret = ""
    for l in big:
        if not l in small:
            ret += l
    return ret

def plus(first, second):
    return first + second

def same(first, second):
    return sorted(first) == sorted(second)

def inside(big, small):
    for l in small:
        if l not in big:
            return False
    return True

def assign(scramble):
    # sorted(words, key=len)
    known = {}
    # 1, 7, 4, (235), (069), 8
    sorted_segments = sorted(scramble.split(), key=len)
    # !!! flip these !!! and make the numbers strings!
    known.update({1: sorted_segments[0]})
    known.update({7: sorted_segments[1]})
    known.update({4: sorted_segments[2]})
    known.update({8: sorted_segments[9]})
    two_three_five = [sorted_segments[3], sorted_segments[4], sorted_segments[5]]
    zero_six_nine = [sorted_segments[6], sorted_segments[7], sorted_segments[8]]
    # 9 contains 4 and 7
    # 0 contains 1
    # 6 remains
    # 3 contains 1
    # 5 contains (4 - 1)? OR 9 does not contain 2/ 6 does not contain 5
    # 2 OR 5 remains

    return known

def make_number(display):
    n = ""
    for s in display.split(" "):
        n += known.get(s)
    return int(n)

def part1(parsed):
    ret = 0
    for p in parsed:        
        ret += len([display for display in p[1].split(' ') if unique_identifier(display)])
    return ret

def part2(parsed):
    # each line of parsed is [str, str]
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
