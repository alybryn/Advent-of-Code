import pathlib
import sys

SAMPLE_ANSWER_1 = 2
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return list(puzzle_input)

def move(c):
    if c == '^':
        return (1, 0)
    elif c == 'v':
        return (-1, 0)
    elif c == '<':
        return (0, -1)
    else:
        return (0, 1)

def part1(parsed):
    # print(parsed)
    #     (ud, lr)
    curr = (0, 0)
    houses = {curr}
    for c in parsed:
        m = move(c)
        curr = (curr[0] + m[0], curr[1] + m[1])
        houses.add(curr)
    # print(houses)
    return len(houses)

def part2(parsed):
    # print(parsed)
    santas_turn = True
    robot = (0,0)
    real = (0,0)
    houses = {robot, real}
    for c in parsed:
        # print(f"santa {real} : robot {robot}")
        m = move(c)
        if santas_turn:
            real = (real[0] + m[0], real[1] + m[1])
            houses.add(real)
        else:
            robot = (robot[0] + m[0], robot[1] + m[1])
            houses.add(robot)
        santas_turn = not santas_turn
    return len(houses)

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