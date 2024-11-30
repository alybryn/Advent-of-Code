import pathlib
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    ret = {}
    for line in puzzle_input.split():
        a, b = line.split("-")
        up = ret.get(a,[])
        up.append(b)
        ret.update({a:up})
        up = ret.get(b,[])
        up.append(a)
        ret.update({b:up})
    return ret

def findPath(path, system):
    ret = []
    for step in lookAhead(path, system):
        if step != 'end':
            ret+=(findPath(traverse(path,step),system))
        else:
            ret.append(str(f"{path},{step}"))
    return ret

def lookAhead(path, system):
    ret = []
    # print(f"{path}:{path.split(',')[-1]}")
    for s in system.get(path.split(',')[-1]):
        if s.isupper() or str(path).find(s) == -1:
            ret.append(s)
    return ret

def traverse(path, step):
    return str(f"{path},{step}")

def part1(parsed):
    # print(parsed)
    return len(findPath('start',parsed))

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