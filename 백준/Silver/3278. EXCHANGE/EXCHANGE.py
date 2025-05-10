import sys
input = sys.stdin.readline

mark, dollar = 100, 0
for _ in range(int(input())):
    B, S = map(int, input().split())
    mark, dollar = max(mark, dollar * 100 / S), max(dollar, mark * B / 100)
print(f"{mark:.2f}")