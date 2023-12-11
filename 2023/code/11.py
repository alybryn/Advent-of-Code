import pathlib
import sys

SAMPLE_ANSWER_1 = 374
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return [line for line in puzzle_input.split()]

def expand_vertical(input):
    ret = {}
    return ret

def expand_horizontal(input):
    ret = {}
    return ret

def find_galaxies(input):
    ret = {}
    return ret

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1]-p1[1])

def part1(parsed):
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