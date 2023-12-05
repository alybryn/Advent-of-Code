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

    # returns unchanged: [NumberRange], mapped: NumberRange?
    def map_range(self, range):
        self_last = self._srs + self._rl - 1
        # case no overlap
        if range.start > self_last or range.last < self._srs:
            # this will be thrown out but there's
            # an assert expecting it anyway
            return [range], None
        # case range extends past map
        if range.start > self._srs and range.last > self_last:
            diff = range.start - self._srs
            return NumberRange.diff(range, NumberRange(range.start, self._rl - diff)), NumberRange(self._drs+diff, self._rl-diff)
        # case map extends past range
        if range.start < self._srs and range.last < self_last:
            diff = self._srs - range.start
            return NumberRange.diff(range, NumberRange(range.start+diff, range.length-diff)), NumberRange(self._drs, range.length-diff)
        # case range within map
        if self._srs <= range.start and range.last <= self_last:
            diff = range.start - self._srs
            return [], NumberRange(self._drs + diff, range.length)
        # case map within range
        if range.start <= self._srs and self_last <= range.last:
            diff = self._srs - range.start
            return NumberRange.diff(range, NumberRange(range.start+diff, self._rl)), NumberRange(self._drs, self._rl)
        print("should be unreachable, (AlmanacMap.map_range())")
        print(self)
        print(range)

    def __repr__(self) -> str:
        return f'AlmanacMap: {self._drs}, {self._srs}, {self._rl}, {self._srs + self._rl - 1}'

class NumberRange():
    def __init__(self, start, range_length) -> None:
        self._start = start
        self._range_length = range_length
        self._last = start + range_length - 1

    @classmethod
    def recombine(cls, range_1, range_2):
        if range_1.start == range_2.end + 1:
            return NumberRange(range_2.start, range_1.length + range_2.length)
        elif range_2.start == range_1.end + 1:
            return NumberRange(range_1.start, range_1.length + range_2.length)     
   
    #usage: AlmanacMap returns a new range
    # arg1: old range ;args: new range
    # returns any range in old not in new
    # new is entirely within old
    # can return 2 NumberRange objects
    # return type list, can be empty
    @classmethod
    def diff(cls, old_range, new_range):
        # same new range can't have any spans not within old
        if old_range.length == new_range.length:
            return []
        # simple, share start
        elif old_range.start == new_range.start:
            return [NumberRange(new_range.last+1, old_range.last-new_range.last)]
        # simple, share end
        elif old_range.last == new_range.last:
            return [NumberRange(old_range.start, new_range.start-old_range.start)]
        # complicated, two returns, just same as above
        else:
            return [NumberRange(new_range.last+1, old_range.last-new_range.last),
                    NumberRange(old_range.start, new_range.start-old_range.start)]

    # >
    @classmethod
    def __gt__(cls, lh, rh):
        return lh.start > rh.start

    @property
    def start(self):
        return self._start
    
    @property
    def last(self):
        return self._last
    
    @property
    def length(self):
        return self._range_length
    
    def __repr__(self) -> str:
        return f'NumberRange: {self._start}, {self._range_length}, {self._last}'

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