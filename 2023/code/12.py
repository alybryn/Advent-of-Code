import pathlib
import sys

SAMPLE_ANSWER_1 = 21
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    lines = [line.split(' ') for line in puzzle_input.split('\n')]
    return [[line[0],[int(l) for l in line[1].split(',')]] for line in lines]

def count_damage(spring):
    ret = []
    count = 0
    for c in spring:
        if c == '#':
            count += 1
        else:
            if count != 0:
                ret.append(count)
                count = 0
    if count != 0:
        ret.append(count)
    return ret

def unknown_indices(spring):
    ret = []
    for i in range(len(spring)):
        if spring[i] == '?':
            ret.append(i)
    return ret

def make_two_strings(string, index):
    """takes a string, returns 2 altered at index"""
    return [''.join([string[:index], c, string[index+1:]]) for c in ['.', '#']]

def make_two_for_each(strings, index):
    """for each provided string, returns 2 altered at index"""
    ret = []
    for string in strings:
        ret.extend(make_two_strings(string, index))
    return ret

def all_iterations(spring):
    """Create all possible spring strings"""
    springs = [spring]
    indices = unknown_indices(spring)
    for i in indices:
        make_two_for_each(springs, i)

def count_minimum_damaged_comprehensive(spring):
    ret = []
    count = 0
    counting_damaged = False
    for c in spring:
        if c in ['?', '.']:
            if counting_damaged:
                ret.append(count)
                count = 0
                counting_damaged = False
            count += 1
        if c == '#':
            if not counting_damaged:
                ret.append(0 - count)
                count = 0
                counting_damaged = True
            count +=1
    if count != 0:
        if not counting_damaged:
            count = 0 - count
        ret.append(count)
    return ret

def count_maximum_damaged_comprehensive(spring):
    ret = []
    count = 0
    counting_damaged = False
    for c in spring:
        if c == '.':
            if counting_damaged:
                ret.append(count)
                count = 0
                counting_damaged = False
            count += 1
        elif c in ['#', '?']:
            if not counting_damaged:
                counting_damaged = True
                if count != 0:
                    ret.append(0 - count)
                    count = 0
            count +=1
    if count != 0:
        if not counting_damaged:
            count = 0 - count
        ret.append(count)
    return ret

def count_maximum_damaged_summary(spring):
    return sum([i for i in count_maximum_damaged_comprehensive(spring) if i > 0])

def part1(parsed):
    ret = 0
    for record in parsed:
        spring = record[0]
        known = record[1]
        print(spring)
        print(count_minimum_damaged(spring))
        print(count_maximum_damaged(spring))
    return parsed

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