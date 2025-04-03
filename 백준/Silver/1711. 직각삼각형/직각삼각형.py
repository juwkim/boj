import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    nums = [[*map(int, input().split())] for _ in range(N)]
    d2 = [[0] * N for _ in range(N)]
    for i in range(N - 1):
        x1, y1 = nums[i]
        for j in range(i + 1, N):
            x2, y2 = nums[j]
            d2[i][j] = (x1 - x2) ** 2 + (y1 - y2) ** 2
    ans = 0
    for p1 in range(N - 2):
        for p2 in range(p1 + 1, N - 1):
            for p3 in range(p2 + 1, N):
                a, b, c = d2[p1][p2], d2[p1][p3], d2[p2][p3]
                if a + b == c or a + c == b or b + c == a:
                    ans += 1
    return ans

print(solve())