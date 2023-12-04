import pathlib
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    ret = {}
    lines = puzzle_input.split()
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            ret.update({(i, j): int(lines[i][j])})
    return ret

def adjacent(x, y):
    matrix = [(0,1), (0,-1), (1,0), (-1,0)]
    return [(x + m[0], y + m[1]) for m in matrix]

def define_basin(low_point, floor_map):
    checked = set()
    ret_update, checked_update = basin_neighbors(low_point, floor_map, checked)
    return ret_update

def basin_neighbors(point, floor_map, checked):
    ret = set()
    for n in adjacent(point):
        if n not in checked:
            checked.add(n)
            ret_update, checked_update = basin_neighbors(n, floor_map, checked)
            ret.update(ret_update)
            checked.update(checked_update)
            if floor_map.get(n, 9) != 9:
                ret.add(n)
    return (ret, checked)

def find_low_points(floor_map):
    low_points = []
    for k in floor_map.keys():
        height = floor_map.get(k)
        lowest = True
        for xy in adjacent(k[0], k[1]):
            # if xy-point _higher_or_level_with_ k-point.
            if floor_map.get(xy, 10) <= height:
                lowest = False
        if lowest:
            low_points.append(k)
    for low in low_points:
        print(f"{floor_map.get(low)} at {low}")
    low_points_values = [floor_map.get(l) for l in low_points]

def risk_level(n):
    return n + 1

def part1(parsed):
    # find low points
    low_points = find_low_points(parsed)
    # sum low points + len(lowpoints)
    return sum([risk_level(l) for l in low_points_values])

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