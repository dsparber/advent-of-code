from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from itertools import count
from typing import Iterable, override, Optional

from math import prod, lcm

from utils import run


def solve(input_data: str) -> Iterable[int]:
    modules = parse_modules(input_data)

    counts = {False: 0, True: 0}
    first_high = dict()
    rx_as_target = [module for module in modules.values() if "rx" in module.outputs]
    inputs_of_module_with_target_rx = rx_as_target[0].inputs if rx_as_target else []

    solution_part_1 = None
    solution_part_2 = None

    for button_press in count(start=1, step=1):
        queue = [("button", "broadcaster", False)]

        while queue:
            sender, receiver, signal = queue.pop(0)
            counts[signal] += 1

            if receiver not in modules:
                continue

            new_signal = modules[receiver].process_signal(sender, signal)
            if new_signal is None:
                continue

            if receiver not in first_high and new_signal is True:
                first_high[receiver] = button_press

            for output in modules[receiver].outputs:
                queue.append((receiver, output, new_signal))

        if button_press == 1000:
            solution_part_1 = prod(counts.values())

        if all([module in first_high for module in inputs_of_module_with_target_rx]):
            solution_part_2 = lcm(*map(first_high.get, inputs_of_module_with_target_rx))

        if solution_part_1 and solution_part_2:
            break

    return solution_part_1, solution_part_2


@dataclass
class Module(ABC):
    label: str
    inputs: list[str] = field(default_factory=list)
    outputs: list[str] = field(default_factory=list)

    @abstractmethod
    def process_signal(self, sender: str, is_high: bool) -> Optional[bool]:
        pass


@dataclass
class Broadcast(Module):
    @override
    def process_signal(self, sender: str, is_high: bool) -> bool:
        return is_high


@dataclass
class FlipFlop(Module):
    on: bool = False

    @override
    def process_signal(self, sender: str, is_high: bool) -> Optional[bool]:
        if not is_high:
            self.on = not self.on
            return self.on


@dataclass
class Conjunction(Module):
    inputs_high: dict[str, bool] = field(default_factory=dict)

    @override
    def process_signal(self, sender: str, is_high: bool) -> bool:
        self.inputs_high[sender] = is_high
        return not all([self.inputs_high.get(inpt, False) for inpt in self.inputs])


def parse_modules(input_data: str) -> dict[str, Module]:
    modules = dict()
    for line in input_data.splitlines():
        label, outputs = line.split(" -> ")
        outputs = outputs.split(", ")
        if label[0] == "%":
            module = FlipFlop(label[1:])
        elif label[0] == "&":
            module = Conjunction(label[1:])
        else:
            module = Broadcast(label)

        module.outputs = outputs
        modules[module.label] = module

    # Set inputs
    for label, module in modules.items():
        for output in module.outputs:
            if output in modules:
                modules[output].inputs.append(label)

    return modules


run(solve)
