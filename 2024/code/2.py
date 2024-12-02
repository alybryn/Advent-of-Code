import pathlib
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return [line for line in puzzle_input.split()]

def reportReport(report):
    report = [int(r) for r in report.split(' ')]
    rr = set()
    for i in range(0, len(report)-1):
        rr.add(report[i] - report[i+1])
    return rr

def isSafe(report):
    rr = reportReport(report)
    return rr <= {-1,-2,-3} or rr <= {1,2,3}

def part1(parsed):
    print(parsed)
    c=0
    for report in parsed:
        if isSafe(report):
            c += 1
    return c

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
