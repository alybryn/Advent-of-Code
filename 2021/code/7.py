import pathlib
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return [int(line) for line in puzzle_input.split(',')]

def fuel_equation(diff):
    ret = 0
    for i in range(diff + 1):
        ret += i
    return ret

def fuel_loop(crabs, part = 1):
    lowest = min(crabs)
    highest = max(crabs)
    fuel_economy = None
    # move each crab to each position between min and max
    for i in range(lowest, highest + 1):
        fuel = 0
        for crab in crabs:
            diff = abs(i - crab)
            if part == 2:
                diff = fuel_equation(diff)
            fuel += diff
            if fuel_economy is not None and fuel > fuel_economy:
                break

        if fuel_economy is None:
            fuel_economy = fuel

        if fuel < fuel_economy:
            fuel_economy = fuel
    return fuel_economy

def part1(parsed):
    return fuel_loop(parsed)

def part2(parsed):
    # for i in range(4):
    #     print(f"{i} is {fuel_equation(i)}")
    return fuel_loop(parsed, 2)

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