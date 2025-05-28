import sys
input = sys.stdin.readline
import bisect

for tc in range(1, int(input()) + 1):
    N = int(input())
    R = sorted((r, i) for i, r in enumerate(map(int, input().split())))
    result = [0] * N
    j = 0
    for i in range(N):
        while j + 1 < N and R[j + 1][0] <= 2 * R[i][0]:
            j += 1
        if i == j:
            if j:
                result[R[i][1]] = R[j - 1][0]
            else:
                result[R[i][1]] = -1
        else:
            result[R[i][1]] = R[j][0]
    print(f"Case #{tc}:", *result)