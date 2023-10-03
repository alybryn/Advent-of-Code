import pathlib
import re
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

LIGHTS = {}
def set_lights(default=False):
    for i in range(0, 1000):
        for j in range(0, 1000):
            LIGHTS[(i, j)] = default

def get_lit():
    ret = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            ret += LIGHTS[i, j]
    return ret

def parse(puzzle_input):
    #output format: [((s0, s1), (e0, e1), todo)]
    ret = []
    for line in puzzle_input.split("\n"):
        # parse the input
        #print(line)
        # regex it:
        '''
        turn on _,_ through _,_
        turn off _,_ through _,_
        toggle _,_ through _,_
        '''
        #get numbers
        nums = re.findall("[0-9]+", line)
        #print(nums)
        start = (int(nums[0]), int(nums[1]))
        end = (int(nums[2]), int(nums[3]))
        '''
        turn on 
        turn off 
        toggle 
        '''
        if re.match("turn on", line):
            ret.append((start, end, on))
        elif re.match("turn off", line):
            ret.append((start, end, off))
        elif re.match("toggle", line):
            ret.append((start, end, toggle))
    return ret

# added Bool for part2 action
def off(x, y, part2):
    if part2:
        # turn down by 1
        ...
    else:
        LIGHTS[(x, y)] = False
    
def on(x, y, part2):
    if part2:
        ...
    else:
        LIGHTS[(x, y)] = True

def toggle(x, y, part2):
    if part2:
        ...
    else:
        LIGHTS[(x, y)] = not LIGHTS[(x, y)]

# what_do((m,n)), (o,p), action)
def loop(start, end, action, part2=False):
    for i in range(start[0], end[0] +1):
        for j in range(start[1], end[1] + 1):
            #print(f"{i},{j}")
            action(i, j, part2)

def part1(parsed):
    set_lights()
    for input in parsed:
        loop(input[0], input[1], input[2])
    return get_lit()

def part2(parsed):
    # set_lights()
    # loop2(parsed)
    # return get_lit()
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