import sys
input = sys.stdin.readline

for tc in range(1, 1 + int(input())):
    N, M, A = map(int, input().split())
    if A > N * M:
        print(f"Case #{tc}: IMPOSSIBLE")
        continue
    ans = "IMPOSSIBLE"
    for x1 in range(N + 1):
        for x2 in range(N + 1):
            for y1 in range(M + 1):
                for y2 in range(M + 1):
                    if A == abs(x1 * y2 - x2 * y1):
                        ans = f"0 0 {x1} {y1} {x2} {y2}"
                        break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break
    print(f"Case #{tc}: {ans}")