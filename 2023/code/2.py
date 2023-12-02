from enum import Enum
import pathlib
import re
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input

    # return a dict in form: 
    # {<game #> : [{Color.RED: #, Color.BLUE: #, Color.GREEN: #}
    ret = {}
    for line in puzzle_input.split('\n'):
        game_number_part, rounds_part = line.split(': ')
        game_number = int(re.match(r'^Game (?P<number>\d+)', game_number_part).groupdict().get('number'))
        # print(f'number: {game_number}')
        
        rounds_part_list = rounds_part.split('; ')
        rounds_list = []
        for i in range(len(rounds_part_list)):
            # round #i
            round_dict = {}
            for pick in (re.findall(r'(\d+) (red|green|blue)', rounds_part_list[i])):
                round_dict.update({pick[1]: int(pick[0])})
            rounds_list.append(round_dict)
        ret.update({game_number: rounds_list})

    return ret

class Color(str, Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

def part1(parsed):
    cubes = {Color.RED: 12, Color.GREEN: 13, Color.BLUE: 14}
    # print(parsed)
    # sum possible game ids
    ret = 0
    possible = True
    # iterate on game keys
    for k in parsed.keys():
        game = parsed.get(k)
        for round in game:
            for color in Color:
                if round.get(color, 0) > cubes.get(color):
                    possible = False
        if possible:
            ret += k
        possible = True

    return ret

def part2(parsed):
    # find the greatest number called of each color in each game
    ret = 0
    for k in parsed.keys():
        minimum = {Color.RED: 0, Color.GREEN: 0, Color.BLUE: 0}
        game = parsed.get(k)
        for round in game:
            for color in Color:
                m = round.get(color, 0)
                if m > minimum.get(color):
                    minimum.update({color: m})
            power = 1
            for color in Color:
                power = power * minimum.get(color)
        ret += power
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