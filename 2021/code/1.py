import pathlib
import sys

# ADVENT_OF_CODE_YEAR_DIR = pathlib.Path.home().joinpath("Documents", "programming", "Advent of Code", "2021")
# DATA_FILE = ADVENT_OF_CODE_YEAR_DIR.joinpath("data", "1.txt")


SAMPLE_ANSWER_1 = 7
SAMPLE_ANSWER_2 = 5

def parse(puzzle_input):
    # parse the input
    return [line for line in puzzle_input.split()]

def simpleIncrease(depths):
    ret = 0
    for i in range(1, len(depths)):
        if depths[i-1] < depths[i]:
            ret += 1
    return ret

def threeSlideIncrease(depths):
    sums = []
    for i in range(2, len(depths)):
        sums.append(sum([depths[i-2], depths[i-1], depths[i]]))
    print(sums)
    return simpleIncrease(sums)

def part1(parsed):
    ret = 0
    for i in range(0, len(parsed) - 1):
        # if i < 2 or len(parsed) - i < 4:
        #     print(f"Comparing {parsed[i]} with {parsed[i + 1]}")
        if parsed[i] == parsed[i + 1]:
            print("something here?")
        if parsed[i] < parsed[i + 1]:
            ret += 1
    return ret

def part2(parsed):
    return threeSlideIncrease(parsed)

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