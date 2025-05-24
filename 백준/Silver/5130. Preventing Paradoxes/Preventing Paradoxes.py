import sys
input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    N = int(input())
    ps = [tuple(map(int, input().split())) for _ in range(N)]
    area = sum(ps[i-1][0] * ps[i][1] - ps[i][0] * ps[i-1][1] for i in range(N))
    print(f"Data Set {tc}:\n{('RIGHT', 'LEFT')[area > 0]}\n")