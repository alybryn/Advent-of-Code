import functools
import pathlib
import re
import sys

SAMPLE_ANSWER_1 = 21
SAMPLE_ANSWER_2 = 525152

def parse(puzzle_input):
    # parse the input
    return [line.split(' ') for line in puzzle_input.split('\n')]

@functools.cache
def record_match(spring, record):
    if spring == '':
        if record == '':
            return 1
        else:
            return 0
    elif record == '':
        if '#' in record:
            return 0
        else:
            return 1
    list_record = [int(i) for i in record.split(',')]
    record_element_removed = ','.join(str(c) for c in list_record[1:])
    # regex things start
    # consume an extra . or ? for spacing
    matcher = r'^[#|?]{'+str(list_record[0])+'}[.|?]'
    if spring[0] == '.':
        return record_match(spring[1:], record)
    elif spring[0] == '#': # has to match
        if re.match(matcher, spring):
            return record_match(spring[list_record[0]+1:], record_element_removed)
        else:
            return 0
    else: # if spring[0] == '?': # optional match
        if re.match(matcher, spring):
            return record_match(spring[list_record[0]+1:], record_element_removed) + record_match(spring[1:], record)
        else:
            return record_match(spring[1:], record)

def mult_five(input):
    return ['?'.join([input[0]]*5), ','.join([input[1]]*5)]

def part1(parsed):
    ret = 0
    for record in parsed:
        # spring = record[0]
        # known = record[1]
        # for iteration in all_iterations(spring):
        #     if count_damage(iteration) == known:
        #         ret += 1
        match = record_match(record[0], record[1])
        print(f'{record}, {match}')
        ret += match
    return ret

def part2(parsed):
    return 0
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