from collections import defaultdict
from time import perf_counter
from typing import Iterable

from utils import run


def get_options_to_keep(options: set[tuple]) -> set[tuple]:

    options_to_keep = set()
    for this in sorted(options, reverse=True):

        keep_this = True
        for _, to_keep in enumerate(options_to_keep):
            if all(e >= m for e, m in zip(to_keep, this)):
                # there exists a better option, do not add this
                keep_this = False
                break

        if keep_this:
            options_to_keep.add(this)

    return options_to_keep


def geodes_for_blueprint(blueprint: dict, days: int = 24) -> int:
    robots = (1, 0, 0, 0)
    minerals = (0, 0, 0, 0)
    states = {robots: {minerals}}

    mineral_types = ['ore', 'clay', 'obsidian', 'geode']
    max_minerals_needed = [max([costs.get(t, 0) for costs in blueprint.values()]) for t in mineral_types]
    max_minerals_needed[3] = int(1e12)

    def build_robot(current_robots: tuple, current_minerals: list):
        # Do not build a robot
        yield current_robots, current_minerals.copy()

        # Build robot of type t
        for i, t in enumerate(mineral_types):
            new_robots = list(current_robots)
            new_minerals = current_minerals.copy()
            for mineral_type, amount in blueprint[t].items():
                new_minerals[mineral_types.index(mineral_type)] -= amount
            if min(new_minerals) >= 0 and current_robots[i] < max_minerals_needed[i]:
                new_robots[i] += 1
                yield tuple(new_robots), new_minerals

    start = perf_counter()
    for _ in range(days):
        new_states: dict[tuple, set[tuple]] = defaultdict(set)
        for robots, mineral_options in states.items():
            for minerals in mineral_options:
                for new_robots, new_minerals in build_robot(robots, list(minerals)):

                    # Mine
                    for i in range(4):
                        new_minerals[i] += robots[i]

                    new_states[new_robots].add(tuple(new_minerals))

        for key, mineral_options in new_states.items():
            new_states[key] = get_options_to_keep(mineral_options)
        states = new_states

        # keys_to_keep = get_options_to_keep(new_states.keys())
        # states = {k: get_options_to_keep(v) for k, v in new_states.items() if k in keys_to_keep}
    max_geodes = max([minerals[3] for mineral_options in states.values() for minerals in mineral_options])
    return max_geodes


def solve(input_data: str) -> Iterable[int]:

    blueprints = list()
    for line in input_data.split('\n'):
        blueprint = dict()
        blueprints.append(blueprint)
        costs_text = line.split(':')[1]
        for cost_text in costs_text.split('.'):
            if cost_text:
                parts = cost_text.strip().split(' ')
                robot_type = parts[1]
                blueprint[robot_type] = dict()
                cost, resource_type = parts[4:6]
                blueprint[robot_type][resource_type] = int(cost)
                if len(parts) > 7:
                    cost, resource_type = parts[7:9]
                    blueprint[robot_type][resource_type] = int(cost)

    quality_level_sum = 0
    for nr, blueprint in enumerate(blueprints, 1):
        max_geodes = geodes_for_blueprint(blueprint)
        quality_level_sum += nr * max_geodes

    yield quality_level_sum

    geodes_product = 1
    for blueprint in blueprints[:3]:
        max_geodes = geodes_for_blueprint(blueprint, days=32)
        geodes_product *= max_geodes

    yield geodes_product


run(solve)
