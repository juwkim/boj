import sys
import bisect
input = sys.stdin.readline

N = int(input())
board = [*zip(*sorted([*map(int, input().split())] for _ in range(N)))]
nums = board[1]
dp = [-1000000001]
p = []

for num in nums:
    if num > dp[-1]:
        dp.append(num)
        p.append(len(dp) - 1)
    else:
        idx = bisect.bisect_left(dp, num)
        dp[idx] = num
        p.append(idx)

len_dp = len(dp) - 1
print(N - len_dp)

temp, idx = [], -1
while len_dp:
    if p[idx] == len_dp:
        len_dp -= 1
        temp.append(board[0][idx])
    idx -= 1

ans = sorted(set(board[0]) - set(temp))
print(*ans, sep="\n")