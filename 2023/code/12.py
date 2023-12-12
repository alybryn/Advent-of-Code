import pathlib
import sys

SAMPLE_ANSWER_1 = 21
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    lines = [line.split(' ') for line in puzzle_input.split('\n')]
    return [[line[0],[int(l) for l in line[1].split(',')]] for line in lines]

def count_minimum_damaged(spring):
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
        ret.append(count)
    return ret


def part1(parsed):
    ret = 0
    for record in parsed:
        spring = record[0]
        known = record[1]
        print(spring)
        print(count_minimum_damaged(spring))
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