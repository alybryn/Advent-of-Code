import pathlib
import sys

SAMPLE_ANSWER_1 = 18
SAMPLE_ANSWER_2 = None

X = "x"
M = "m"
A = "a"
S = "s"

def parse(puzzle_input):
    # parse the input
    return [[l for l in line] for line in puzzle_input.split()]

# check XMAS and SAMX... 
# can share Ss and Xs...
def confirm(x,m,a,s):
    return x == X and m == M and a == A and s == S

# horizontal
# horizontal reversed
def searchH(p):
    m = 0
    for i in len(p):
        for j in len(p[0]):
            if p[i][j] == X or p[i][j] == S:
                return None

def buildH(puzzle):
    m = []
    for i in range(0, len(p)):
        s = ""
        for j in range(0, len(p[0])):
            s += puzzle[i][j]
        m.append(s)
    return m
    
# vertical
# vertical reversed
def buildV(puzzle):
    m = []
    for i in range(0, len(p[0])):
        s = ""
        for j in range(0, len(p)):
            s += puzzle[j][i]
        m.append(s)
    return m

# diagonal down right
# diagonal up left
#x=y,x=y+1,x=y+2...
def buildDD(puzzle):
    # start len(p[0]), 0
    for j in 

# diagonal up right
# diagonal down left

def part1(parsed):
    print(parsed)
    return parsed

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
