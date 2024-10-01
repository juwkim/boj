import sys
input = sys.stdin.readline

for tc in range(1, 1 + int(input())):
    N = int(input())
    m = [*map(int, input().split())]
    ans1 = sum(max(0, m[i] - m[i + 1]) for i in range(N - 1))
    rate = max(max(0, m[i] - m[i + 1]) for i in range(N - 1))
    ans2 = sum(min(rate, m[i]) for i in range(N - 1))
    print(f'Case #{tc}: {ans1} {ans2}')