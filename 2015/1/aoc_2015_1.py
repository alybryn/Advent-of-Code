import pathlib
import sys

SAMPLE_ANSWER_1 = [0, 0, 3, 3, 3, -1, -1, -3, -3]
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return [line for line in puzzle_input.split()]

def move(ch):
    if ch == "(":
        return 1
    else:
        return -1

def part1(parsed):
    floors = []
    for line in parsed:
        floor = 0
        for ch in list(line):
            #print(f"{ch}\n")
            floor += move(ch)
        floors.append(floor)
    return floors

def part2(parsed):
    ans = []
    for line in parsed:
        floor = 0
        ch_list = list(line)
        for i in range(len(ch_list)):
            floor += move(ch_list[i])
            if floor == -1:
                ans.append(i+1)
                break
            if i == len(ch_list) - 1:
                ans.append(-1)
    return ans

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