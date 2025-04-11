import sys
input = sys.stdin.readline

for _ in range(int(input())):
    for i in range(1, int(input()) + 1):
        x, y = map(int, input().split())
        print(i, x + 1, y + 3 * 10**8)