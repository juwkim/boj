import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M, Q = g()
Map = [input() for _ in range(N)]

hints = []
for _ in range(Q):
    num, pp = input().split()
    hints.append((int(num) - 1, pp))

buf = [i for i in range(N) if all(Map[i][num] == hint for num, hint in hints)]
if len(buf) == 1:
    print("unique")
    print(buf[0] + 1)
else:
    print("ambiguous")
    print(len(buf))