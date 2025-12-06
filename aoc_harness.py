import sys
import time
import os
import subprocess


def puzzle_main(*solvers):
    if len(sys.argv) == 1:
        in_filename = get_input_path(solvers[0])
    elif len(sys.argv) == 2:
        in_filename = sys.argv[1]
    else:
        raise ValueError("Expected 0 or 1 arguments")

    if in_filename == "-":
        in_file = sys.stdin
    else:
        in_file = open(in_filename, "r", encoding="utf-8")

    input_data = in_file.read()
    for solver in solvers:
        t1 = time.perf_counter()
        result = solver(input_data)
        t2 = time.perf_counter()
        print(result)
        duration = t2 - t1
        print(f"time: {duration*1000.0:.03f} ms")


def get_input_path(solver):
    mod_name = solver.__module__
    mod = sys.modules[mod_name]
    mod_basename = os.path.split(mod.__file__)[-1].removesuffix(".py")
    project_root = os.path.join(*os.path.split(__file__)[:-1])
    input_file_name = os.path.join(project_root, "input", f"{mod_basename}.txt")
    if os.path.exists(input_file_name):
        return input_file_name

    cookie_file = os.path.join(project_root, ".aoc-cookie")
    if os.path.exists(cookie_file):
        day_num = int(mod_basename.removeprefix("day"))
        url = f"https://adventofcode.com/2025/day/{day_num}/input"
        os.makedirs(os.path.join(project_root, 'input'), exist_ok=True)
        subprocess.check_call(["curl", "-o", input_file_name, "-b", cookie_file, url])
        return input_file_name
    else:
        raise RuntimeError("Can't download input without cookie file")
