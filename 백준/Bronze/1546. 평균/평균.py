import sys
N = int(input())
scores = list(map(int, sys.stdin.readline().split()))
print(sum(scores) * 100 / (N * max(scores)))