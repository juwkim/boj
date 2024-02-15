import sys
input = lambda: sys.stdin.readline().rstrip()

for tc in range(1, 1 + int(input())):
    N, F = input().split()
    N, F = int(N), float(F)
    px = [0]
    for c in map(int, input()):
        px.append(px[-1] + c)
    ans, d = 0, 1e9
    for i in range(N):
        for j in range(i + 1, N + 1):
            cur = abs(F - (px[j] - px[i]) / (j - i))
            if cur < d:
                ans, d = i, cur
    print(f"Case #{tc}: {ans}")