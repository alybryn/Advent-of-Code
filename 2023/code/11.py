import pathlib
import sys

SAMPLE_ANSWER_1 = 374
# for 10, 100
SAMPLE_ANSWER_2 = 1030, 8410

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

def apply_expansions(input_galaxies, expansions, expand_by=2):
    vertical_expansions = expansions.get('v')
    horizontal_expansions = expansions.get('h')
    ret = []
    for galaxy in input_galaxies:
        # account for already present row, needs replaced, not added to
        expand_vert = sum([1 for e in vertical_expansions if e < galaxy[0]]) * (expand_by-1)
        expand_hori = sum([1 for e in horizontal_expansions if e < galaxy[1]]) * (expand_by-1)
        # (print(expand_vert, expand_hori))
        ret.append((galaxy[0] + expand_vert, galaxy[1] + expand_hori))
    return ret

def pair_and_measure(galaxies_list):
    ret = 0
    for i in range(len(galaxies_list)):
        for j in range(i, len(galaxies_list)):
            ret += manhattan_distance(galaxies_list[i], galaxies_list[j])
    return ret

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1]-p2[1])

def part1(parsed):
    galaxies_list, wh = parsed
    expansions = find_expansions(parsed)
    # expanded = apply_expansions(galaxies_list, wh, expansions)
    expanded = apply_expansions(galaxies_list, expansions)
    return pair_and_measure(expanded)

def part2(parsed):
    galaxy_list, wh = parsed
    expansions = find_expansions(parsed)
    expanded = apply_expansions(galaxy_list, expansions, 1_000_000)
    return pair_and_measure(expanded)

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