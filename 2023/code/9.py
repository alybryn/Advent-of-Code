import pathlib
import sys

SAMPLE_ANSWER_1 = 114
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return [[int(l) for l in line.split(' ')] for line in puzzle_input.split('\n')]

def get_difference(input):
    ret = []
    for i in range(len(input)-1):
        ret.append(input[i+1] - input[i])
    return ret

def get_sequences(input):
    result = []
    for sequence in input:
        this_result = [sequence[-1]]
        # alt: while s.count(0) != len(s):
        while False in [s == 0 for s in sequence]:
            sequence = get_difference(sequence)
            this_result.append(sequence[-1])
        result.append(this_result)
    return result

def part1(parsed):
    return get_sequences(parsed)

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