import sys
input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    m, n = map(int, input().split())
    ans = m * n + (2**.5 - 1) * (n % 2 + m % 2 == 2)
    print(f"Scenario #{tc}:\n{ans:.2f}\n")