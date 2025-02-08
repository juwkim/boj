import sys
input = sys.stdin.readline

L_max = 100
for tc in range(1, 1 + int(input())):
    B, L, N = map(int, input().split())
    nums = [[[0] * (j + 1) for j in range(i)] for i in range(L_max + 1)]
    nums[1][0][0] = 3 * B
    l, drop = 1, True
    while drop:
        drop = False
        for i in range(l):
            for j in range(i + 1):
                if nums[l][i][j] > 1:
                    drop = True
                    left = nums[l][i][j] - 1
                    nums[l][i][j] = 1
                    nums[l + 1][i][j] += left / 3
                    nums[l + 1][i + 1][j] += left / 3
                    nums[l + 1][i + 1][j + 1] += left / 3
        l += 1
    i = int((2 * N + 0.25) ** 0.5 - 0.5 - 1e-9)
    j = N - i * (i + 1) // 2 - 1
    print(f"Case #{tc}: {nums[L][i][j] * 250}")