import pathlib
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    ret = {}
    for line in puzzle_input.split():
        a, b = line.split("-")
        # don't add 'start' to anyone's neighbors
        if b != 'start':
            up = ret.get(a,[])
            up.append(b)
            ret.update({a:up})
        if a != 'start':
            up = ret.get(b,[])
            up.append(a)
            ret.update({b:up})
    return ret

def findPath1(path, system):
    ret = []
    for step in lookAhead1(path, system):
        if step != 'end':
            ret+=(findPath1(traverse(path,step),system))
        else:
            ret.append(str(f"{path},{step}"))
    return ret

def lookAhead1(path, system):
    ret = []
    # print(f"{path}:{path.split(',')[-1]}")
    for s in system.get(path.split(',')[-1]):
        if s.isupper() or str(path).find(s) == -1:
            ret.append(s)
    return ret

# pathDouble -> (path, hasDouble)
def findPath2(pathD, system):
    ret = []
    # step -> (step, hasDouble)
    # print(lookAhead2(pathD, system))
    for step in lookAhead2(pathD, system):
        if step[0] != 'end':
            ret+=(findPath2((traverse2(pathD, step)),system))
            # print(ret)
        else:
            ret.append(str(f"{pathD[0]},{step}"))
    # print(ret)
    return ret

def lookAhead2(pathD, system):
    ret = []
    path = pathD[0]
    hasDouble = pathD[1]
    # print(f"{path},{hasDouble}")
    for s in system.get(path.split(',')[-1]):
        # print(s)
        if s.isupper():
            ret.append((s,hasDouble))
        else:
            if path.find(s) > -1:
                if not hasDouble:
                    ret.append((s,True))
            else:
                ret.append((s,hasDouble))
    # print(ret)
    return ret

def traverse(path, step):
    return str(f"{path},{step}")

def traverse2(path, step):
    ret = (traverse(path[0],step[0]),step[1])
    # print(ret)
    return ret

def part1(parsed):
    # print(parsed)
    ret = findPath1('start',parsed)
    # print(ret)
    return len(ret)

def part2(parsed):
    ret = findPath2(('start',False),parsed)
    # print(ret)
    return len(ret)

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