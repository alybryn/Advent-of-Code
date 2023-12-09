import pathlib
import sys

SAMPLE_ANSWER_1 = 114
SAMPLE_ANSWER_2 = 2

def parse(puzzle_input):
    # parse the input
    return get_history([[int(l) for l in line.split(' ')] for line in puzzle_input.split('\n')])

def get_difference(input):
    ret = []
    for i in range(len(input)-1):
        ret.append(input[i+1] - input[i])
    return ret

def get_history(input):
    history = []
    for sequence in input:
        this_result = []
        # alt: while s.count(0) != len(s):
        while False in [s == 0 for s in sequence]:
            #first and last difference
            this_result.append((sequence[0], sequence[-1]))
            sequence = get_difference(sequence)
        history.append(this_result)
    return history

# input is [(first, last), ...]
def extrapolate(input):
    prev = (0, 0)
    for n in input[::-1]:
        prev = (n[0] - prev[0], prev[1] + n[1])
    return prev

def collate(input, index):
    ret = 0
    for history in input:
        # history is [(first,last), ...]
        ret += extrapolate(history)[index]
    return ret

def part1(parsed):
    return collate(parsed, 1)

def part2(parsed):
    return collate(parsed, 0)

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