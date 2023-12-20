from collections import namedtuple
from enum import Enum
import pathlib
import sys

SAMPLE_ANSWER_1 = 32000000
SAMPLE_ANSWER_2 = None

class Signal(Enum):
    LOW = 0
    HIGH = 1

class Pulse(namedtuple('Pulse',['signal','destination', 'sender'])):
    def __repr__(self) -> str:
        return f'{self.signal.name} -> {self.destination}'

class Broadcaster():
    def __init__(self, destinations, modules) -> None:
        self._name = 'broadcast'
        self._destinations = destinations
        self._all_modules = modules

    def push_button(self):
        count = 0
        sending = []
        for destination in self._destinations:
            sending.append(Pulse(Signal.LOW,destination, self._name))
        while sending:
            count += len(sending)
            to_send_on = []
            for pulse in sending:
                to_send_on.extend(self._all_modules.get(pulse.destination).receive(pulse))
            sending = to_send_on
        return count
    
    def __repr__(self) -> str:
        return f'Broadcasting to {self._destinations} knowing about:\n' + '\n'.join([str(m) for m in self._all_modules.values()])
def parse(puzzle_input):
    # parse the input
    return [line for line in puzzle_input.split()]

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