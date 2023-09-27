import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
drone = sorted((max(map(abs, g())), i) for i in range(1, N + 1))
if any(drone[i][0] < i + 1 for i in range(N)):
    print(-1)
else:
    print(*[*zip(*drone)][1])
