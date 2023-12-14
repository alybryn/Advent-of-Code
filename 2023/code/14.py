import pathlib
import sys

SAMPLE_ANSWER_1 = 136
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return Platform([list(line) for line in puzzle_input.split()])

class Direction(Enum):
    NORTH = (-1,0)
    SOUTH = (1, 0)
    EAST = (0,1)
    WEST = (0,-1)

    def neighbor(self, coord):
        return self.value[0] + coord[0], self.value[1] + coord[1]
        
class Platform():
    def __init__(self, input) -> None:
        self._southern_edge = len(input)
        self._eastern_edge = len(input[0])
        self._map = {}
        for x in range(self._southern_edge):
            for y in range(self._eastern_edge):
                if input[x][y] != '.':
                    # round is True, square is False, none is None
                    self._map.update({(x,y): input[x][y] == 'O'})

    def tilt(self, direction):
        for k in self._map.keys():
            # round is True, square is False, none is None
            rock = self._map.get(k)
            if rock:
                new = self.tilt_at(direction, k)
                self.update({new: rock})
                # try del later, but not on first pass
                self.update({k: None})

    # args are Direction and location of a round rock
    def tilt_at(self, direction, loc):
        while loc not in self._map.keys():
            pass
        

    def north_load(self):
        ret = 0
        for k in self._map.keys():
            rock = self._map.get(k)
            if rock.is_round:
                ret += self._southern_edge - k[0]
        return ret

    def __str__(self) -> str:
        p = ''
        for x in range(self._southern_edge):
            for y in range(self._eastern_edge):
                r = self._map.get((x, y))
                p += 'O' if r else '.' if r == None else '#'
            p += '\n'
        return p

def part1(parsed):
    return parsed

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