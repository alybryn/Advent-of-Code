import pathlib
import re
import sys

SAMPLE_ANSWER_1 = 18
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return [[l for l in line] for line in puzzle_input.split()]

# check XMAS and SAMX... 
# can share Ss and Xs...
def count(line):
    # no matches? Returns empty list
    return len(re.findall('XMAS',line)) + len(re.findall('SAMX',line))

def buildH(puzzle):
    m = []
    for i in range(0, len(puzzle)):
        s = ""
        for j in range(0, len(puzzle[0])):
            s += puzzle[i][j]
        m.append(s)
    return m
    
# vertical
# vertical reversed
def buildV(puzzle):
    m = []
    for i in range(0, len(puzzle[0])):
        s = ""
        for j in range(0, len(puzzle)):
            s += puzzle[j][i]
        m.append(s)
    return m

# diagonal down right
# diagonal up left
#x=y,x=y+1,x=y+2...
def buildDD(puzzle):
    m = set()
    # start len(p[0]), 0
    for i in range(0,len(puzzle)):
        s=""
        for n in range(i,len(puzzle)):
            # print(f"{n-i},{n},{puzzle[n-i][n]}")
            s += puzzle[n-i][n]#f"({n-i},{n})"
        # print(s)
        m.add(s)
    for i in range(0,len(puzzle)):
        s = ''
        for n in range(0,i+1):
            # print(f"{i-n},{n},{puzzle[i-n][n]}")
            # print(f'{n},{i},{len(puzzle)-1-n},{len(puzzle)-i-1}')
            # s += f"({len(puzzle)-1-i+n},{n})"
            s += puzzle[len(puzzle)-1-i+n][n]
        # print(s)
        m.add(s)
    return list(m)

# diagonal up right
# diagonal down left
def buildDU(puzzle):
    m = set()
    for i in range(0,len(puzzle)):
        s=""
        for n in range(0,i+1):
            # print(f"{i-n},{n},{puzzle[i-n][n]}")
            s += puzzle[i-n][n]
        # print(s)
        m.add(s)
    for i in range(0,len(puzzle)):
        s=''
        for n in range(len(puzzle)-1, i-1,-1):
            s += puzzle[len(puzzle)-1+i-n][n]
        # print(s)
        m.add(s)
    return list(m)
        

def part1(parsed):
    # print(parsed)
    # print(f'{len(parsed)}x{len(parsed[0])}')
    c = 0
    for f in [buildH, buildV, buildDD, buildDU]:
        for line in f(parsed):
            # print(line)
            c += count(line)
        # print('\n')
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
