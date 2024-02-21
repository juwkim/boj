import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    nums = [[*map(int, input().split())] for _ in range(N * N)]
    for i in range(N * N):
        row = bytearray(N * N + 1)
        col = bytearray(N * N + 1)
        for j in range(N * N):
            if nums[i][j] and row[nums[i][j]]:
                return "INCORRECT"
            row[nums[i][j]] = True
            if nums[j][i] and col[nums[j][i]]:
                return "INCORRECT"
            col[nums[j][i]] = True
    for i in range(0, N * N, N):
        for j in range(0, N * N, N):
            square = bytearray(N * N + 1)
            for x in range(N):
                for y in range(N):
                    if nums[i + x][j + y] and square[nums[i + x][j + y]]:
                        return "INCORRECT"
                    square[nums[i + x][j + y]] = True
    return "CORRECT"
print(solve())