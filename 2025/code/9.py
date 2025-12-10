DAY = 9
YEAR = 2025

START = f'/workspaces/Advent of Code/{YEAR}'
SAMPLE_PATH = f'{START}/sample/{DAY}.txt'
SAMPLE_A_PATH = f'{START}/sample/{DAY}a.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH,SAMPLE_A_PATH]
ONLY_DATA = [DATA_PATH]
ALL = [SAMPLE_PATH, DATA_PATH]

RUN = ONLY_SAMPLE

# --------------------------------

import pathlib
import sys

SAMPLE_ANSWER_1 = 50
SAMPLE_ANSWER_2 = 24
SAMPLE_A_ANSWER_1 = 35
SAMPLE_A_ANSWER_2 = 15

def parse(puzzle_input):
    # parse the input
    points = [to_tuple([int(l) for l in line.split(',')]) for line in puzzle_input.split()]
    lines = []
    for i in range(0, len(points)-1):
        lines.append((points[i],points[i+1]))
    lines.append((points[-1],points[0]))
    boxes = []
    while len(points) != 0:
        t1 = points.pop()
        for t2 in points:
            boxes.append((t1,t2))
    return boxes, lines

def to_tuple(two_item_list):
    assert(len(two_item_list)==2)
    return (two_item_list[0],two_item_list[1])

def area(t1, t2):
    return (abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1)

def sides(box):
    p0,p2 = box
    x0 = p0[0]
    x1 = p2[0]
    y0 = p0[1]
    y1 = p2[1]
    return (((x0,y0),(x0,y1)),
            ((x0,y1),(x1,y1)),
            ((x1,y1),(x1,y0)),
            ((x1,y0),(x0,y0)))

# disclaimer, might not actually detect horizonticality
def is_horizontal(line):
    return line[0][0] == line[1][0]

# disclaimer, might not actually detect verticality
def is_vertical(line):
    return line[0][1] == line[1][1]

def linear(c0,c1,c2):
    return c0 < c1 < c2 or c2 < c1 < c0

def intersect(line0, line1):
        #l_,p_,c_
        if is_horizontal(line0) == is_horizontal(line1) or is_vertical(line0) == is_vertical(line1):
            return False
        # perpendicular, not points (all zero lenth lines fall within the space)
        if is_horizontal(line0):
            # line0's x falls within line1's x's
            if linear(line1[0][0], line0[0][0], line1[1][0]):
                # and line0's y's encompass line1's y
                if linear(line0[0][1], line1[0][1], line0[1][1]):
                    return True
        else:
            # line0's y falls within line1's y's
            if linear(line1[0][1], line0[0][1], line1[1][1]):
                # and line0's x's encompass line1's x
                if linear(line0[0][0], line1[0][0], line0[1][0]):
                    return True
        return False

def poly_intersect(line, lines):
    for l in lines:
        if intersect(line,l):
            print(f'{line} does intersect {l}')
            visualize(line,l)
            return True
    return False

def visualize(line1,line2):
    line_1_points = [line1[0],line1[1]]
    line_2_points = [line2[0],line2[1]]
    xs = [line1[0][0],line1[1][0],line2[0][0],line2[1][0]]
    ys = [line1[0][1],line1[1][1],line2[0][1],line2[1][1]]
    ret = ''
    for i in range(min(xs),max(xs)+1):
        for j in range(min(ys),max(ys)+1):
            if (i,j) in line_1_points and (i,j) in line_2_points:
                ret += '#'
            elif (i,j) in line_1_points:
                ret += '1'
            elif(i,j) in line_2_points:
                ret += '2'
            else:
                ret += '.'
        ret += '\n'
    print(ret)

def part1(parsed):
    boxes = parsed[0]
    big = 0
    for box in boxes:
        a = area(box[0], box[1])
        if a > big: big = a
    return big

def part2(parsed):
    boxes,lines = parsed
    big = 0
    for box in boxes:
        box_contained = True
        for side in sides(box):
            if poly_intersect(side,lines):
                box_contained = False
                break
        if box_contained:
            print(f'ok box: {box}')
            a = area(box[0], box[1])
            if a > big: big = a
    return big

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

def run(path):
    print(f'{path}')
    puzzle_input = pathlib.Path(path).read_text().strip()

    solutions = solve(puzzle_input)
    print('\n'.join(str(solution) for solution in solutions))

if __name__ == "__main__":
    for path in RUN:
        run(path)
    for path in sys.argv[1:]:
        run(path)
