import sys
S, M, L = map(int, sys.stdin.read().split())
print("happy" if S + 2 * M + 3 * L >= 10 else "sad")