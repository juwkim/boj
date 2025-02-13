import sys
input = sys.stdin.readline

N = int(input())
nums = [[*map(int, input().split())] for _ in range(N)]
max_time = 1825 * max(H for H, _, _ in nums)
i = 0
while i < max_time:
    for H, R, T in nums:
        hh = i % H
        if R > T:
            if hh > R or hh < T:
                break
        elif R < hh < T:
            break
    else:
        break
    i += 1
if i == max_time:
    print("impossible")
else:
    print(i)