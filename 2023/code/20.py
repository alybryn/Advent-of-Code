from collections import namedtuple
from enum import Enum
import pathlib
import re
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

class FlipFlop():
    def __init__(self, name, destinations) -> None:
        self._name = name
        # ON =True
        self._state = False
        self._destinations = destinations

    def receive(self, pulse):
        if pulse.signal == Signal.LOW:
            to_send = Signal.LOW if self._state else Signal.HIGH
            self._state = not self._state
            ret = []
            for destination in self.destinations:
                ret.append(Pulse(to_send,destination,self._name))
            return ret
        print(f'{self._name} is ignoring Signal.HIGH')
        return []

    def is_reset(self):
        return not self._state
    
    def __repr__(self) -> str:
        return f'{self._name} is {'on' if self._state else 'off'} sending to {self._destinations}'

class Conjunction():
    def __init__(self, name, destinations, senders) -> None:
        self._name = name
        self._destinations = destinations
        self._senders = senders
        self._states = {}
        for sender in self._senders:
            self._states[sender] = Signal.LOW

    def receive(self, pulse):
        self._states.update({pulse.sender: pulse.signal})
        to_send = Signal.HIGH if Signal.LOW in self._states.values() else Signal.HIGH
        ret = []
        for destination in self._destinations:
            ret.append(Pulse(to_send,destination,self._name))
        return ret

    def is_reset(self):
        return Signal.HIGH in self._states.values()
    
    def __repr__(self) -> str:
        return f'{self._name} remembers '+'\n'.join([f'{s} is {self._states[s]}' for s in self._states.keys()]) + f' and sends to {self._destinations}'

def parse(puzzle_input):
    # parse the input
    lines = puzzle_input.split('\n')
    modules = {}
    for line in lines:
        name, destinations = line.split(' -> ')
        destinations = destinations.split(', ')
        if name.startswith('&'):
            name = name.removeprefix('&')
            senders = [sender for sender in [re.match(r'[%|&](.+) -> ', c)[1] for c in lines if name in c] if sender != name]
            modules[name] = Conjunction(name, destinations, senders)
        elif name.startswith('%'):
            name = name.removeprefix('%')
            modules[name] = FlipFlop(name, destinations)
        else:
            assert(name == 'broadcaster')
            broadcaster = Broadcaster(destinations,modules)
    return broadcaster

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