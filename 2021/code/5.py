import pathlib
import re
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    pattern = r'(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)'
    ret = [re.match(pattern, line).groupdict() for line in puzzle_input.split('\n')]
    return ret

class Line():
    def __init__(self, input):
        #{(x, y)}
        self._points = set()
        
        # string defs
        diagonal = 'diagonal'
        horizontal = 'horizontal'
        vertical = 'vertical'

        x2 = int(input.get('x2'))
        y1 = int(input.get('y1'))
        x1 = int(input.get('x1'))
        y2 = int(input.get('y2'))
        dir = diagonal
        if x1 == x2:
            dir = horizontal
        elif y1 == y2:
            dir = vertical

        # sanitize input:
        # fuck's sake only do this if not diagonal
        if dir != diagonal:
            if x1 > x2:
                x2, x1 = x1, x2
            if y1 > y2:
                y2, y1 = y1, y2
        # diagonal version
        else:
            if x1 > x2:
                x2, x1, y2, y1 = x1, x2, y1, y2
        
        # write the rest of the damn function
        if dir == diagonal:
            # pos or neg slope
            if y1 < y2: # pos
                for i in range(x2 - x1 + 1):
                    self._points.add((x1 + i, y1 + i))
            else: # neg
                for i in range(x2 - x1 + 1):
                    self._points.add((x1 + i, y1 - i))
        elif dir == vertical:
            y = y1
            for x in range(x1, x2 + 1):
                self._points.add((x, y))
        else: #horizontal
            x = x1
            for y in range(y1, y2 + 1):
                self._points.add((x, y))

    @property
    def get_points(self):
        return self._points

class VentMap():
    def __init__(self):
        # dict: (x, y): i
        self._points = {}

    def add_line(self, line: Line):
        for p in line.get_points:
            curr = self._points.get(p, 0)
            self._points.update({p: curr + 1})
        
    def print(self):
        for p in self._points.keys():
            print(f"{p}: {self._points.get(p)}")

    def draw(self):
        p = ''
        for r in range(10):
            for c in range(10):
                p += str(self._points.get((c, r), '.'))
            p += '\n'
        print(p)

    
    def count_danger_points(self):
        return len([1 for n in self._points.values() if n > 1])

def part1(parsed):
    my_map = VentMap()
    h_and_v = ([l for l in parsed if l.get('x1') == l.get('x2') or l.get('y1') == l.get('y2')])
    for line in h_and_v:
        #print(line)
        my_map.add_line(Line(line))
    my_map.draw()
    # print(Line({'x1': '3', 'y1': '4', 'x2': '1', 'y2': '4'}).get_points)
    return my_map.count_danger_points()

def part2(parsed):
    my_map = VentMap()
    for line in parsed:
        my_map.add_line(Line(line))
    my_map.draw()
    return my_map.count_danger_points()

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