import pathlib
import sys

SAMPLE_ANSWER_1 = 1928
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    file_system = []

    for i in range(0, len(puzzle_input)//2):
        file_name = i
        free = int(puzzle_input[i*2+1])
        file = int(puzzle_input[i*2])
        for b in range(0, file):
            file_system.append(file_name)
        for b in range(0, free):
            file_system.append(None)
    return file_system

def defrag(file_system):
    while None in file_system:
        temp = file_system.pop()
        if temp == None:
            continue
        # get index of earliest None
        i = file_system.index(None)
        # remove that None
        # insert temp
        file_system[i] = temp

def checksum(file_system):
    ret = 0
    for i in range(0, len(file_system)):
        ret += i * file_system[i]
    return ret

def part1(parsed):
    print(parsed)
    defrag(parsed)
    return checksum(parsed)

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