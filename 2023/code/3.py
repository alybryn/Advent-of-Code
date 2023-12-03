import pathlib
import sys

SAMPLE_ANSWER_1 = 4361
SAMPLE_ANSWER_2 = 467835

def parse(puzzle_input) -> (dict, list, list):
    # parse the input
    lines = puzzle_input.split()
    # print(lines)
    # length = len(lines)
    width = len(lines[0])
    points = {}
    nums = []
    
    for i in range(len(lines)):
        j = 0
        while j < width:
            if lines[i][j].isdigit():
                # start getting number
                n = ''
                p = []
                while lines[i][j].isdigit():
                    n += lines[i][j]
                    p.append((i, j))
                    
                    # overwriting numbers for now
                    points.update({(i, j): '.'})
                    j += 1
                    if j == width:
                        break
                # acutally create and save Nums
                nums.append(Num(int(n),p))
            else:
                points.update({(i, j): lines[i][j]})
                j += 1
    # once quick through the dict:
    gears = []
    for k in points:
        if points.get(k) == "*":
            # check neighbors against nums
            number_neighbors = []
            k_neighbors = xy_neighbors(k)
            for num in nums:
                if num.contains_list(k_neighbors):
                    number_neighbors.append(num)
            if len(number_neighbors) == 2:
                gears.append(Gear(number_neighbors))

    return (points, nums, gears)


def xy_neighbors(pair) -> list:
    # diagonals too
    matrix = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (1,1), (-1,1), (1,-1)]
    return [(pair[0] + m[0], pair[1] + m[1]) for m in matrix]

class Num():
    # val: int, points: [(x,y),...]
    def __init__(self, value: int, points: list):
        self._value = value
        self._points = points
    
    @property
    def neighbors(self):
        ret = set()

        # add neighbors for each point
        for p in self._points:
            for n in xy_neighbors(p):
                # prevention is the best cure:
                if n not in self._points:
                    ret.add(n)
        return ret
    
    @property
    def value(self) -> int:
        return self._value
    
    # def contains(self, point):
    #     return point in self._points

    def contains_list(self, l) -> bool:
        for point in l:
            if point in self._points:
                return True
        return False

class Gear():
    def __init__(self, neighbor_numbers: list):
        self._gear_ratio = neighbor_numbers[0].value * neighbor_numbers[1].value

    @property
    def gear_ratio(self) -> int:
        return self._gear_ratio

def part1(parsed):
    # add part numbers
    ret = 0
    mapping = parsed[0]
    numbers = parsed[1]
    for n in numbers:
        # part numbers are adjacent to non '.' chars
        for p in n.neighbors:
            if mapping.get(p, '.') != '.':
                ret += n.value
                break
    return ret

def part2(parsed):
    ret = 0
    for gear in parsed[2]:
        ret += gear.gear_ratio
    return ret

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