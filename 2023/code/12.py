import pathlib
import sys

SAMPLE_ANSWER_1 = 21
SAMPLE_ANSWER_2 = 525152

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
        springs = make_two_for_each(springs, i)
    return springs

def mult_five(input):
    return ['?'.join([input[0]]*5), input[1]*5]

def part1(parsed):
    ret = 0
    for record in parsed:
        spring = record[0]
        known = record[1]
        for iteration in all_iterations(spring):
            if count_damage(iteration) == known:
                ret += 1
    return ret

def part2(parsed):
    ret = 0
    new_version = []
    for p in parsed:
        new_version.append(mult_five(p))
    new_version = [new_version[1]]
    print(new_version)
    for record in new_version:
        spring = record[0]
        known = record[1]
        for iteration in all_iterations(spring):
            if count_damage(iteration) == known:
                ret += 1
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