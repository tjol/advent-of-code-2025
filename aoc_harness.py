import sys
import time

def puzzle_main(*solvers):
    if len(sys.argv) == 1:
        in_filename = '-'
    elif len(sys.argv) == 2:
        in_filename = sys.argv[1]
    else:
        raise ValueError("Expected 0 or 1 arguments")
    
    if in_filename == '-':
        in_file = sys.stdin
    else:
        in_file = open(in_filename, 'r', encoding='utf-8')
    
    input_data = in_file.read()
    for solver in solvers:
        t1 = time.perf_counter()
        result = solver(input_data)
        t2 = time.perf_counter()
        print(result)
        duration = t2 - t1
        print(f'time: {duration*1000.0:.03f} ms')
