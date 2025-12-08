import runpy
from pathlib import Path
import time


if __name__ == "__main__":
    project_dir = Path(__file__).parent

    t1 = time.perf_counter()

    for i in range(1, 13):
        fn = project_dir / f"day{i:02}.py"
        if fn.exists():
            runpy.run_path(fn, run_name="__main__")

    t2 = time.perf_counter()
    dt = t2 - t1
    print(f"Total runtime: {dt:.5} s")
