DAY = 22

START = f'/workspaces/Advent-of-Code/2024'
SAMPLE_PATH = f'{START}/sample/{DAY}.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]
ALL = [SAMPLE_PATH, DATA_PATH]

RUN = ONLY_SAMPLE

# --------------------------------

import pathlib
import sys

SAMPLE_ANSWER_1 = 37327623
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return [int(line) for line in puzzle_input.splitlines()]

def mix(num, sec_num):
    return num ^ sec_num

def prune(num):
    return num % 16777216

def the_process(num):
    num = prune(mix(num * 64, num))
    num = prune(mix(num // 32, num))
    num = prune(mix(num * 2048, num))
    return num

def two_thousandth(num):
    ret = num
    for _ in range(0,2000):
        ret = the_process(ret)
    return ret

# better plan: save all prices in dictionary 
# indexed by previous price changes, 
# pool keys and iterate to find max

class PriceList:
    def __init__(self):
        self._elements = (None,None,None,None,None)
    
    def add(self, x):
        a,b,c,d,_ = self._elements
        self._elements = (x,a,b,c,d)

    def log(self):
        if self._elements[4]:
            a,b,c,d,e = self._elements
            return[a-b,b-c,c-d,d-e]

def price(num): return num%10

def valid(a,b,c,d):
    return -9+a < 10 and -9+a+b < 10 and -9+a+b+c < 10 and -9+a+b+c+d < 10 and 9+a > -10 and 9+a+b > -10 and 9+a+b+c > -10 and 9 +a+b+c+d > -10

def part1(parsed):
    # print(parsed)
    return sum([two_thousandth(p) for p in parsed])

def part2(parsed):
    price_change_dict = {}
    for seed in parsed:
        num = seed
        change = PriceList()
        seed_dict = {}
        for _ in range(0,2000):
            num = the_process(num)
            change.add(price(num))
            log = change.log()
            if log:
                if log not in price_change_dict:
                    seed_dict[log]=price(num)
        price_change_dict[seed] = seed_dict
    pooled_changes = set([change for changes in price_change_dict.values() for change in changes.values()])
    max_banana = 0
    for change in pooled_changes:
        for seed_dict in price_change_dict.values():
            pass

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