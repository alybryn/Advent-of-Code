import pathlib
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    l1 = []
    l2 = []
    for line in puzzle_input.split():
        a, b = line.split("   ")
        l1.append(a)
        l2.append(b)
    l1.sort()
    l2.sort()
    return (l1,l2)

def part1(parsed):
    print(parsed)
    (a,b) = parsed
    diff = 0
    for i in len(a):
        diff += math.abs(a[i] - b[i])
    return diff

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
