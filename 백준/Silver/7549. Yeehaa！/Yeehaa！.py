import sys
import math
input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    R, n = input().split()
    sin_a = math.sin(math.pi / int(n))
    r = float(R) * sin_a / (1 + sin_a)
    print(f"Scenario #{tc}:\n{r:.3f}\n")