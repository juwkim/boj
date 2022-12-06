R, C = map(int, input().split())
a = [[*map(int, input().split())] for _ in range(C)]
b = [[*map(int, input().split())] for _ in range(R)]
if a == [*map(list, zip(*b))][::-1]:
    print('|>___/|        /}', '| O < |       / }', '(==0==)------/ }', '| ^  _____    |', '|_|_/     ||__|', sep='\n')
else:
    print('|>___/|     /}', '| O O |    / }', '( =0= )""""  \\', '| ^  ____    |', '|_|_/    ||__|', sep='\n')   