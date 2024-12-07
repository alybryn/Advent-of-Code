import pathlib
import sys

SAMPLE_ANSWER_1 = 3749
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    ret = {}
    for line in puzzle_input.split("\n"):
        result, values = line.split(": ")
        values = [int(value) for value in values.split(" ")]
        ret.update({int(result):values})
    return ret

def try_add(result, values):
    if len(values) == 1:
        return result == values[0]
    new_values = [values[0] + values[1]] + values[2:]
    return try_add(result, new_values) or try_mult(result, new_values)

def try_mult(result, values):
    if len(values) == 1:
        return result == values[0]
    new_values = [values[0] * values[1]] + values[2:]
    return try_add(result, new_values) or try_mult(result, new_values)

def part1(parsed):
    print(parsed)
    ret = 0
    for result, values in parsed.items():
        if try_add(result, values) or try_mult(result, values):
            ret += result
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
