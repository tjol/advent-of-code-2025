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


def day11part2(input_: str):
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

    svr_dac = count_paths("svr", "dac")
    dac_fft = count_paths("dac", "fft")
    fft_out = count_paths("fft", "out")
    svr_fft = count_paths("svr", "fft")
    fft_dac = count_paths("fft", "dac")
    dac_out = count_paths("dac", "out")
    svr_dac_fft_out = svr_dac * dac_fft * fft_out
    srv_fft_dac_out = svr_fft * fft_dac * dac_out
    return svr_dac_fft_out + srv_fft_dac_out


def parse_graph(input_: str):
    graph = {}
    for line in input_.strip().splitlines():
        from_node, to_nodes_s = line.split(": ")
        to_nodes = to_nodes_s.split()
        graph[from_node] = to_nodes

    return graph


TEST_INPUT_1 = """
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

TEST_INPUT_2 = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""


def test_part1():
    assert day11part1(TEST_INPUT_1) == 5


def test_part2():
    assert day11part2(TEST_INPUT_2) == 2


if __name__ == "__main__":
    from aoc_harness import puzzle_main

    puzzle_main(day11part1, day11part2)
