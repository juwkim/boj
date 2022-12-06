import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

input()
card = {*g()}
input()
for num in g():
    print(+(num in card), end=' ')