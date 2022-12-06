import sys
input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: [*map(int, input().split())]

p, g = MIS()
Map = {}
for _ in range(p):
    party, num = input().split()
    a, b = num.split('.')
    num = int(a) * 10 + int(b)
    Map[party] = num
for _ in range(1, 1 + g):
    *partys, op, num = input().split()
    
    Sum = 0
    for i in range(0, len(partys), 2):
        Sum += Map[partys[i]]
    if op == '=':
        op = '=='

    if eval(''.join([str(Sum), op, num + '0'])):
        print(f'Guess #{_} was correct.')
    else:
        print(f'Guess #{_} was incorrect.')