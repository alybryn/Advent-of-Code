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

# def minus(big, small):
#     ret = ""
#     for l in big:
#         if not l in small:
#             ret += l
#     return ret

def plus(first, second):
    return first + second

# def same(first, second):
#     return sorted(first) == sorted(second)

def sanitize(n):
    return sorted(n)

def inside(big, small):
    for l in small:
        if l not in big:
            return False
    return True

def assign(scramble):
    # sorted(words, key=len)
    # keyed by 1, 2, 3, etc
    # REFACTOR: remove updates to known that are not used
    known = {}
    # keyed by abc, dc, etc
    known_ret = {}
    # 1, 7, 4, (235), (069), 8
    # sorted_segments = sorted(scramble.split(), key=len)
    sorted_segments = [str(sorted(s)) for s in sorted(scramble.split(), key=len)]
    # # sanizite inputs here
    # sorted_sorted_segments = []
    # for s in sorted_segments:
    #     sorted_sorted_segments.append(sanitize(s))

    # !!! flip these !!! and make the numbers strings!
    known.update({1: sorted_segments[0]})
    known_ret.update({sorted_segments[0]: '1'})
    known.update({7: sorted_segments[1]})
    known_ret.update({sorted_segments[1]: '7'})
    known.update({4: sorted_segments[2]})
    known_ret.update({sorted_segments[2]: '4'})
    known.update({8: sorted_segments[9]})
    known_ret.update({sorted_segments[9]: '8'})
    two_three_five = [sorted_segments[3], sorted_segments[4], sorted_segments[5]]
    zero_six_nine = [sorted_segments[6], sorted_segments[7], sorted_segments[8]]
    # 9 contains 4 and 7
    four_plus_seven = plus(known.get(4), known.get(7))
    for n in zero_six_nine:
        if inside(n, four_plus_seven):
            known.update({9: n})
            known_ret.update({n: '9'})
            break
    
    zero_six_nine.remove(known.get(9))

    # print(f"just checking: {zero_six_nine}")

    # 0 contains 1
    for z in zero_six_nine:
        if inside(z, known.get(1)):
            known.update({0: z})
            known_ret.update({z: '0'})
            break
    zero_six_nine.remove(known.get(0))
    # 6 remains
    known.update({6: zero_six_nine[0]})
    known_ret.update({zero_six_nine[0]: '6'})
    # 3 contains 1
    for t in two_three_five:
        if inside(t, known.get(1)):
            known.update({3:t})
            known_ret.update({t:'3'})
    # !! remove the three
    two_three_five.remove(known.get(3))
    
    # 9 contains 5. SO DOES 6!!!
    if inside(known.get(9), two_three_five[1]):
        known.update({2:two_three_five[0]})
        known_ret.update({two_three_five[0]:'2'})
        known.update({5:two_three_five[1]})
        known_ret.update({two_three_five[1]:'5'})
    # 2 OR 5 remains
    else:
        known.update({2:two_three_five[1]})
        known_ret.update({two_three_five[1]:'2'})
        known.update({5:two_three_five[0]})
        known_ret.update({two_three_five[0]:'5'})

    return known_ret

# pass display and dictionary
def make_number(display, known):
    n = ""
    for s in display.split(" "):
        # print(s)
        n += known.get(str(sorted(s)))
    return int(n)

def part1(parsed):
    ret = 0
    for p in parsed:        
        ret += len([display for display in p[1].split(' ') if unique_identifier(display)])
    return ret

def part2(parsed):
    # each line of parsed is [str, str]
    add = 0
    for line in parsed:
        known = assign(line[0])
        add += make_number(line[1], known)
    return add

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
