import hashlib
import pathlib
import random
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return puzzle_input

def test(key, zeros):
    satisfied = False
    i = 0
    while not satisfied:
        i += 1

        hexed = hashlib.md5(f"{key}{i}".encode()).hexdigest()
        satisfied = is_hex_satisfactory(hexed, zeros)
    return i

def is_hex_satisfactory(hex, zeros):
    check = list(hex)
    for i in range(0, zeros):
        if check[i] != '0':
            return False
    return True

def part1(parsed):
    return test(parsed, 5)

def part2(parsed):
    return test(parsed, 6)
 
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