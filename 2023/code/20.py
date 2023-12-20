from collections import namedtuple
from enum import Enum
import pathlib
import re
import sys

SAMPLE_ANSWER_1 = 32000000
SAMPLE_ANSWER_2 = None

class Signal(str,Enum):
    LOW = 'low'
    HIGH = 'high'

class Pulse(namedtuple('Pulse',['signal','destination', 'sender'])):
    def __repr__(self) -> str:
        return f'{self.sender} -{self.signal.name.lower()}-> {self.destination}'

class Broadcaster():
    def __init__(self, destinations, modules) -> None:
        self._name = 'broadcaster'
        self._destinations = destinations
        self._all_modules = modules

    def push_button(self):
        high_count = 0
        low_count = 1
        sending = []
        for destination in self._destinations:
            sending.append(Pulse(Signal.LOW,destination, self._name))
        while sending:
            signal_summation = [p.signal for p in sending]
            high_count += signal_summation.count(Signal.HIGH)
            low_count += signal_summation.count(Signal.LOW)
            to_send_on = []
            for pulse in sending:
                destination = self._all_modules.get(pulse.destination)
                if destination:
                    to_send_on.extend(destination.receive(pulse))
            sending = to_send_on
        return {Signal.HIGH:high_count, Signal.LOW:low_count}
    
    def push_button_for_record(self):
        record = []
        sending = []
        for destination in self._destinations:
            sending.append(Pulse(Signal.LOW,destination, self._name))
        while sending:
            record.extend(sending)
            to_send_on = []
            for pulse in sending:
                destination = self._all_modules.get(pulse.destination)
                if destination:
                    to_send_on.extend(destination.receive(pulse))
            sending = to_send_on
        return record
    
    def push_the_button_a_lot(self, n):
        signal_counts = {Signal.HIGH: 0, Signal.LOW:0}
        for _ in range(n):
            more_counts = self.push_button()
            for s in Signal:
                signal_counts[s] += more_counts[s]
        return signal_counts
    
    def find_period_of(self, specific_pulse):
        self.reset()
        count = 0
        sending = []
        for destination in self._destinations:
            sending.append(Pulse(Signal.LOW,destination,self._name))
        while True:
            record = self.push_button_for_record()
            count += 1
            if specific_pulse in record:
                return count

    def reset(self):
        for module in self._all_modules.values():
            module.reset()

    def __repr__(self) -> str:
        return f'Broadcasting to {self._destinations} knowing about:\n' + '\n'.join([str(m) for m in self._all_modules.values()])

class FlipFlop():
    def __init__(self, name, destinations) -> None:
        self._name = name
        # ON =True
        self._state = False
        self._destinations = destinations

    def receive(self, pulse):
        ret = []
        if pulse.signal == Signal.LOW:
            to_send = Signal.LOW if self._state else Signal.HIGH
            self._state = not self._state
            for destination in self._destinations:
                ret.append(Pulse(to_send,destination,self._name))
        return ret

    def reset(self):
        self._state = False
    
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
        to_send = Signal.HIGH if Signal.LOW in self._states.values() else Signal.LOW
        ret = []
        for destination in self._destinations:
            ret.append(Pulse(to_send,destination,self._name))
        return ret

    def reset(self):
        for k in self._states.keys():
            self._states[k] = Signal.LOW
    
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
    ret = parsed.push_the_button_a_lot(1000)
    return ret[Signal.HIGH] * ret[Signal.LOW]

def part2(parsed):
    ret = 1
    fv = parsed.find_period_of(Pulse(Signal.HIGH,'sq','fv'))
    kk = parsed.find_period_of(Pulse(Signal.HIGH,'sq','kk'))
    vt = parsed.find_period_of(Pulse(Signal.HIGH,'sq','vt'))
    xr = parsed.find_period_of(Pulse(Signal.HIGH,'sq','xr'))
    return fv * kk * vt * xr

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