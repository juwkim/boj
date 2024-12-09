import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, S, E = map(int, input().split())
    if abs(S - E) == N - 1:
        print(0)
    elif abs(S - E) == 1 or S in (1, N):
        print(1)
    else:
        print(2)