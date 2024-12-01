import pathlib
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    dots, instructions = puzzle_input.split('\n\n')
    for dot in dots.split():
        print(f'dot:{dot}')
    instructions = [i for i in instructions.split('\n')]
    return (dots, instructions)

def fold(x, y):
    return

def part1(parsed):
    print(parsed)
    return 0

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