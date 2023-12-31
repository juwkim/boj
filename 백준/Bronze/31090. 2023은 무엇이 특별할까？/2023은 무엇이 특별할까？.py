import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    N = int(input())
    r = N % 100
    if r and (N + 1) % r == 0:
        print("Good")
    else:
        print("Bye")