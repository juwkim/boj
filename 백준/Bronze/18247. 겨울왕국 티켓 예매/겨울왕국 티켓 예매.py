import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(4 + 11 * M if N >= 12 and M >= 4 else -1)