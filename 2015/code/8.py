import pathlib
import sys

# code: 23
# mem:  11
# diff: 12
SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return [line for line in puzzle_input.split()]

def string_count(input):
    length = 0
    escape_mode = False
    skip_counter = 0
    # skip wrapping ""
    for i in range(1, len(input)-1):
        if escape_mode:
            if input[i] in ['\"', '\\']:
                escape_mode = False
            else:
                skip_counter += 1
                if skip_counter == 3:
                    skip_counter = 0
                    escape_mode = False
        else:
            length += 1
            if input[i] == '\\':
                escape_mode = True
    return length

def encode_string(input):
    #start with enclosing quotes
    length = 2
    for c in list(input):
        if c in ['\"', '\\']:
            length += 2
        else:
            # print(f"{c} requires no extra encoding")
            length += 1
    # print(f"{input} is encoded in {length} characters")
    return length


def part1(parsed):
    code = 0
    memory = 0
    for l in parsed:
        code += len(l)
        memory += string_count(l)
    return code - memory

def part2(parsed):
    code = 0
    reencode = 0
    for l in parsed:
        code += len(l)
        # print(encode_string(l))
        reencode += encode_string(l)
    return reencode - code

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