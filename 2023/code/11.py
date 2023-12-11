import pathlib
import sys

SAMPLE_ANSWER_1 = 374
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input, only galaxies
    lines = [[c for c in list(line)] for line in puzzle_input.split()]
    ret = []
    wh = len(lines)
    # for r in range(wh):
    #     for c in range(wh):
    #         ret.update({(r, c): lines[r][c]})
    for r in range(wh):
        for c in range(wh):
            if lines[r][c] == '#':
                ret.append((r, c))
    return ret, wh

# def expand_vertical(input):
#     input_map, input_width, input_height = input
#     ret = {}
#     for c in range(input_width):
#         for r in range(input_height):
#             pass
#     return ret

# def expand_horizontal(input):
#     input_map, input_width, input_height = input
#     ret = {}
#     for r in range(input_height):
#         for c in range(input_width):
#             pass
#     return ret

# def find_galaxies(input):
#     input_map, input_wh = input
#     ret = []
#     for r in range(input_wh):
#         for c in range(input_wh):
#             if input_map.get((r, c)) == '#':
#                 ret.append((r, c))
#     return ret


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1]-p1[1])

def print_dict(to_print):
    max_key = max(to_print.keys())
    p = ''
    for i in range(max_key[0]):
        for j in range(max_key[1]):
            p += to_print.get((i, j))
        p += '\n'
    print(p)

def part1(parsed):
    galaxies_list, wh = parsed
    # print_dict(galaxy_map)
    # print(find_galaxies(parsed))
    return parsed

def part2(parsed):
    galaxy_map, wh = parsed
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