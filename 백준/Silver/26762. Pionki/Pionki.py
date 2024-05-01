import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [input() for _ in range(N)]
r = [l.count('#') for l in board]
c = [l.count('#') for l in zip(*board)]
print(sum(r) + sum(c) - max(r) - max(c))