import functools


def day11part1(input_: str):
    graph = parse_graph(input_)

    @functools.cache
    def count_paths(from_node, to_node):
        paths = 0
        for next_node in graph.get(from_node, []):
            if next_node == to_node:
                paths += 1
            else:
                paths += count_paths(next_node, to_node)
        return paths

    return count_paths("you", "out")


def parse_graph(input_: str):
    graph = {}
    for line in input_.strip().splitlines():
        from_node, to_nodes_s = line.split(": ")
        to_nodes = to_nodes_s.split()
        graph[from_node] = to_nodes

    return graph


TEST_INPUT = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""


def test_part1():
    assert day11part1(TEST_INPUT) == 5


if __name__ == "__main__":
    from aoc_harness import puzzle_main

    puzzle_main(day11part1)
