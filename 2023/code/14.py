from functools import cache
import pathlib
import sys

SAMPLE_ANSWER_1 = 136
SAMPLE_ANSWER_2 = 64

def parse(puzzle_input):
    return puzzle_input
    # don't parse the input

def print_section(section):
    p = ''
    for v in section:
        p += 'O' if v else '.' if v == None else '#'
    print(p)

def north_load(platform):
    ret = 0
    platform = [line for line in platform.split('\n')]
    for x in range(len(platform)):
        for y in range(len(platform[0])):
            if platform[x][y] == 'O':
                ret += len(platform) - x
    return ret

@cache
def spin(platform):
    return tilt_east(tilt_south(tilt_west(tilt_north(platform))))

# platform is a string
@cache
def tilt_north(platform):
    platform = [''.join(list(f)) for f in zip(*[list(c) for c in platform.split('\n')])]
    platform = [fall_down(l) for l in platform]
    platform = '\n'.join(''.join(f) for f in zip(*[list(p) for p in platform]))
    return platform

@cache
def tilt_west(platform):
    platform = platform.split('\n')
    platform = [fall_down(l) for l in platform]
    platform = '\n'.join(platform)
    return platform

@cache
def tilt_south(platform):
    return tilt_north(platform[::-1])[::-1]

@cache
def tilt_east(platform):
    return tilt_west(platform[::-1])[::-1]

@cache
def fall_down(section):
    section = list(section)
    for i in range(len(section)):
        if section[i] == 'O':
            next_i = i
            while next_i - 1 >= 0 and section[next_i - 1] == '.':
                next_i = next_i-1
            section[next_i] = 'O'
            if i != next_i:
                section[i] = '.'
    return ''.join(section)
 
def part1(parsed):
    return north_load(tilt_north(parsed))

def part2(parsed):
    platform = parsed
    last_north_load = north_load(platform)
    cycles = 1_000_000_000
    # cycles = 3
    for _ in range(cycles):
        platform = spin(platform)
    return north_load(platform)

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