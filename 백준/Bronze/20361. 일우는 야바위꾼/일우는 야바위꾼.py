import sys
N, X, K = map(int, input().split())
shell_game = [list(map(int, i.split())) for i in sys.stdin.read().split('\n')]
for move in shell_game:
    if X in move:
        X = sum(move) - X
print(X)