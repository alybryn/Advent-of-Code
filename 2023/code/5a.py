import pathlib
import re
import sys

SAMPLE_ANSWER_1 = 35
SAMPLE_ANSWER_2 = 46

def parse(puzzle_input):
    # parse the input
    lines = puzzle_input.split('\n\n')
    seeds = []
    maps = []
    for line in lines:
        if re.match(r'^seeds:', line):
            seeds = [int(l) for l in line.split(' ')[1:]]
        else:
            ints = [[int(i) for i in l.split(' ')] for l in line.split('\n')[1:]]
            maps.append([AlmanacMap(i[0], i[1], i[2]) for i in [f for f in ints]])

    return seeds, maps

class AlmanacMap():
    def __init__(self, destination_range_start, source_range_start, range_length) -> None:
        self._drs = destination_range_start
        self._srs = source_range_start
        # range does this for me
        # self._sr_end = source_range_start + range_length - 1
        self._rl = range_length
    
    def map(self, input):
        if input in range(self._srs, self._srs + self._rl):
            # print(f'\t{input} is in {self._srs} - {self._srs + self._rl - 1}')
            diff = input - self._srs
            return self._drs + diff
        # print(f'\t{input} not in {self._srs} - {self._srs + self._rl - 1}')

    # def un_map(self, output):
    #     if output in range(self._drs, self._drs + self._rl):
    #         diff = output - self._drs
    #         return self._srs + diff

    def __repr__(self) -> str:
        return f'AlmanacMap: {self._drs}, {self._srs}, {self._rl}, {self._srs + self._rl - 1}'

class NumberRange():
    def __init__(self, start, range_length) -> None:
        self._start = start
        self._range_length = range_length

    # def contains(self, seed):
    #     return seed in range(self._start, self._start+self._range_length)
    
    def map_all(self, mapses):
        ret = map_a_seed(self._start, mapses)
        for seed in range(self._start+1, self._start+self._range_length):
            result = map_a_seed(seed, mapses)
            if result < ret:
                ret = result
        return ret
    
    def apply_map(self, map):
        

def map_a_seed(input, mapses):
    num = input
    for maps in mapses:
        # print(num)
        becomes = None
        for map in maps:
            # print(f'\t{map}')
            becomes = map.map(num)
            if becomes:
                break
        if becomes:
            num = becomes
    # print(f'Mapped seed {input} to loc {num}')
    return num

# def map_a_loc(output, mapses):
#     num = output
#     for maps in mapses[::-1]:
#         becomes = None
#         for map in maps:
#             becomes = map.un_map(num)
#             if becomes:
#                 break
#         if becomes:
#             num = becomes
#     return num

def part1(parsed):
    seeds = parsed[0]
    mapses = parsed[1]
    ret = []
    for seed in seeds:
        ret.append(map_a_seed(seed, mapses))
    return min(ret)

def part2(parsed):
    # reimagine seeds as ranges
    seeds = parsed[0]
    seed_ranges = []
    # seeds_to_map = set()
    i = 0
    while i < len(seeds):
        seed_ranges.append(NumberRange(seeds[i], seeds[i+1]))
    #     for seed in range(seeds[i], seeds[i] + seeds[i+1]):
    #         seeds_to_map.add(seed)
    #         # print(f'adding seed {seed}')
        i += 2
    mapses = parsed[1]
    # ret = map_a_seed(seeds[0], mapses)
    # for seed in seeds_to_map:
    #     result = map_a_seed(seed, mapses)
    #     if result < ret:
    #         ret = result
    # rets = []
    # ret, loc = map_a_loc(0, mapses), 0
    # for i in range(1, 90):
    #     rets.append((map_a_loc(i, mapses), i))
    return seed_ranges

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