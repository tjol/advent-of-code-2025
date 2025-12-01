import sys

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
        result = solver(input_data)
        print(result)
