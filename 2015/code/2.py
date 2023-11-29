import pathlib
import sys

SAMPLE_ANSWER_1 = 101
SAMPLE_ANSWER_2 = 48

def parse(puzzle_input):
    # parse the input
    # return a list of lists [[l,w,h]...]
    ls = [line.split('x') for line in puzzle_input.split()]
    ret = []
    for l in ls:
        ret.append((int(l[0]), int(l[1]), int(l[2])))
    return ret

def part1(parsed):
    paper = []
    for line in parsed:
        # find the three sides
        sides = [
            line[0] *line[1],
            line[1] *line[2],
            line[0] *line[2]]
        # find the min for slack
        slack = min(sides)
        paper.append(2*sum(sides)+slack)
    # print(paper)
    return sum(paper)

def part2(parsed):
    ribbon = []
    for line in parsed:
        #find the smallest face
        faces = [line[0] + line[1],
                 line[1] + line[2],
                 line[0] + line[2]]
        ribbon.append(min(faces) * 2)
        #find the volume
        ribbon.append(line[0] * line[1] * line[2])
    # print(ribbon)
    return sum(ribbon)

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