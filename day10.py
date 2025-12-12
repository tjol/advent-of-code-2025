import re
import operator
from functools import reduce

PATTERN = re.compile(r"^\[([#.]+)\] ((?:\([0-9,]+\) )+)\{([0-9,]+)\}$")


def day10part1(input_: str):
    result = 0
    for line in input_.strip().splitlines():
        lights, buttons, _ = parse_machine_desc(line.strip())
        steps = find_least_presses(lights, buttons)
        result += len(steps)

    return result

def day10part2(input_: str):
    result = 0
    for line in input_.strip().splitlines():
        _, buttons, joltages = parse_machine_desc(line.strip())
        print('---', line)
        steps = find_cheapest_joltage(joltages, buttons)
        print('-->', steps)
        result += steps

    return result


def parse_machine_desc(line):
    m = PATTERN.match(line.strip())
    light_diagram = m.group(1)
    lights = reduce(
        operator.or_, ((c == "#") << i for (i, c) in enumerate(light_diagram))
    )
    button_list = m.group(2)
    buttons = []
    for button_desc in button_list.split():
        bit_indices = map(int, button_desc[1:-1].split(","))
        buttons.append(reduce(operator.or_, (1 << i for i in bit_indices)))
    joltage_info = m.group(3)
    joltages = list(map(int, joltage_info.split(",")))
    return lights, buttons, joltages


def find_least_presses(light_pattern, buttons):
    operations = {button: [button] for button in buttons}
    while light_pattern not in operations:
        old_ops = list(operations.items())
        for pattern1, sequence1 in old_ops:
            for pattern2, sequence2 in old_ops:
                new_pattern = pattern1 ^ pattern2
                if new_pattern != 0 and (
                    new_pattern not in operations
                    or len(operations[new_pattern]) > len(sequence1) + len(sequence2)
                ):
                    operations[new_pattern] = [*sequence1, *sequence2]
    return operations[light_pattern]


def find_cheapest_joltage(joltage_target, buttons):
    n = len(joltage_target)
    m = len(buttons)
    button_names = [chr(ord('a') + i) for i in range(m)]
    sums = []
    for i, jolts in enumerate(joltage_target):
        operands = {button_names[k] for (k, button) in enumerate(buttons) if button & (1 << i)}
        sums.append((jolts, operands))

    max_jolts = max(joltage_target)
    bounds = {btn: (0, max_jolts) for btn in button_names}

    def _substitute(sums, bounds, button, value):
        del bounds[button]
        for (i, (total, operands)) in enumerate(sums):
            if button in operands:
                sums[i] = (total - value, operands - {button})

    def _solve(sums, bounds):
        if len(bounds) == 0:
            return {}
        solution = {}
        # Update bounds based on sums
        while True:
            any_updated_1 = False
            for (total, operands) in sums:
                while True:
                    any_updated_2 = False
                    for operand in operands:
                        others = operands - {operand}
                        our_max = total - sum(bounds[b][0] for b in others)
                        our_min = total - sum(bounds[b][1] for b in others)
                        prev_min, prev_max = bounds[operand]
                        new_bounds = max(prev_min, our_min), min(prev_max, our_max)
                        if new_bounds != (prev_min, prev_max):
                            if new_bounds[1] < new_bounds[0]:
                                return None
                            any_updated_2 = True
                            bounds[operand] = new_bounds
                    if any_updated_2:
                        any_updated_1 = True
                    else:
                        break
            # print(bounds)
            if not any_updated_1:
                break
        
        btn, rng = min(bounds.items(), key=lambda kv: kv[1][1] - kv[1][0])
        if rng[0] > rng[1]:
            return None
        elif rng[0] == rng[1]:
            sums = sums[:]
            _substitute(sums, bounds, btn, rng[0])
            solution[btn] = rng[0]
            rest_of_solution = _solve(sums, bounds)
            if rest_of_solution is None:
                return None
            else:
                solution.update(rest_of_solution)
                return solution
        else:
            # split the range and search further
            mid = rng[0] + (rng[1] - rng[0]) // 2
            candidates = []
            for (a, b) in [(rng[0], mid), (mid+1, rng[1])]:
                new_bounds = dict(**bounds)
                new_bounds[btn] = (a, b)
                maybe_solution = _solve(sums, new_bounds)
                if maybe_solution is not None:
                    candidates.append(maybe_solution)

            if candidates:
                best_candidate = min(candidates, key=lambda sol: sum(sol.values()))
                solution.update(best_candidate)
                return solution
            else:
                return None

    solution = _solve(sums, bounds)
    return sum(solution.values())




TEST_INPUT = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""


def test_part1():
    assert day10part1(TEST_INPUT) == 7

def test_part2():
    assert day10part2(TEST_INPUT) == 33


def test_parse_line():
    assert parse_machine_desc(
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}"
    ) == (0b01000, [0b11101, 0b1100, 0b10001, 0b111, 0b11110], [7, 5, 12, 7, 2])


def test_example_1():
    lights, buttons, _ = parse_machine_desc(
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
    )
    steps = find_least_presses(lights, buttons)
    assert len(steps) == 2


def test_example_1_p2():
    _, buttons, joltages = parse_machine_desc(
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
    )
    steps = find_cheapest_joltage(joltages, buttons)
    assert steps == 10


if __name__ == "__main__":
    from aoc_harness import puzzle_main

    puzzle_main(day10part1, day10part2)
