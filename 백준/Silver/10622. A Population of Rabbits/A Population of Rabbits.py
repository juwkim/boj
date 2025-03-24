import sys
input = sys.stdin.readline

for tc in range(1, 1 + int(input())):
    D, R, M = map(int, input().split())
    rabbits = [1] + [0] * (D - 1)
    for _ in range(M - 1):
        rabbits = [sum(rabbits[1:R])] + rabbits[:-1]
    print(f"Case #{tc}: {sum(rabbits)}")