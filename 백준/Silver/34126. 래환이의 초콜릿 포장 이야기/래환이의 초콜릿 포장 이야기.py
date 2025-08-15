import sys
input = sys.stdin.readline

for _ in range(int(input())):
    A, B, C = map(int, input().split())
    print((C + 1 >> 1) * 3 + max(0, A + 2 * B + 1 - (C & 1) * 3 >> 1))