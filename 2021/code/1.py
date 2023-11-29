import pathlib
import sys

# ADVENT_OF_CODE_YEAR_DIR = pathlib.Path.home().joinpath("Documents", "programming", "Advent of Code", "2021")
# DATA_FILE = ADVENT_OF_CODE_YEAR_DIR.joinpath("data", "1.txt")


SAMPLE_ANSWER_1 = 7
SAMPLE_ANSWER_2 = 5

def parse(puzzle_input):
    # parse the input
    return [line for line in puzzle_input.split()]

def part1(parsed):
    ret = 0
    comps = 0
    l = len(parsed)
    for i in range(1, l):
        #print(f"comparing {parsed[i-1]} and {parsed[i]}")
        comps += 1
        if parsed[i - 1] < parsed[i]:
            #print(f"{parsed[i-1]} < {parsed[i]}")
            ret += 1
        #else:
            #print(f"{parsed[i-1]} > {parsed[i]}")

    print(f"comps: {comps}, l: {l}")
    return ret

def part2(parsed):
    return 31

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