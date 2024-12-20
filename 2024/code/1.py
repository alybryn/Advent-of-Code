import pathlib
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    left = []
    right = []
    for line in puzzle_input.split('\n'):
        l, r = line.split("   ")
        left.append(int(l))
        right.append(int(r))
    left.sort()
    right.sort()
    return (left,right)

def part1(parsed):
    (left,right) = parsed
    diff = 0
    for i in range(0,len(left)):
        diff += abs(left[i] - right[i])
    return diff

def part2(parsed):
    (left,right) = parsed
    ret = 0
    for l in left:
        count = 0
        for r in right:
            if l == r:
                count += 1
        ret += l * count
    return ret

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
