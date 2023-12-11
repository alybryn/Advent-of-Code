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

def find_expansions(input):
    input_galaxies, wh = input
    vert_expansion = []
    hori_expansion = []
    for i in range(wh):
        expand_vert = True
        expand_hori = True
        for j in range(wh):
            if (i, j) in input_galaxies:
                expand_vert = False
            if (j, i) in input_galaxies:
                expand_hori = False
        if expand_hori:
            hori_expansion.append(i)
        if expand_vert:
            vert_expansion.append(i)
    return {'v': vert_expansion, 'h': hori_expansion}

def apply_expansions(input):
    input_galaxies, wh, expansions = input
    vertical_expasions = expansions.get('v')
    horizontal_expasions = expansions.get('h')

    expand_vert_by = 0
    ret = []

    for r in range(wh):
        if r in vertical_expasions:
            expand_vert_by +=1
        expand_hori_by = 0
        for c in range(wh):
            if c in horizontal_expasions:
                expand_hori_by += 1
            if (r, c) in input_galaxies:
                ret.append((r+expand_vert_by, c+expand_hori_by))
    # might not end square, ret is list, width, height
    return ret, wh+len(horizontal_expasions), wh+len(vertical_expasions)

def pair_and_measure(galaxies_list):
    ret = 0
    for i in range(len(galaxies_list)):
        for j in range(i, len(galaxies_list)):
            ret += manhattan_distance(galaxies_list[i], galaxies_list[j])
    return ret

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1]-p2[1])

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
    print(galaxies_list)
    print(manhattan_distance((6, 1),(11, 5)))
    return pair_and_measure(apply_expansions((galaxies_list, wh, find_expansions(parsed)))[0])

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