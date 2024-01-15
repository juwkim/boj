import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
nums = g()
s = -1
start, end = {}, {}
for i in range(N):
    if s != -1:
        if nums[i] == 0:
            end[s] = i - 1
            start[i - 1] = s
            s = -1
    else:
        if nums[i] == 1:
            s = i
if s != -1:
    end[s] = N - 1
    start[N - 1] = s

for _ in range(M):
    s = input()
    if s == "0":
        print(len(start))
    else:
        _, i = map(int, s.split())
        i -= 1
        if nums[i] == 1:
            continue
        nums[i] = 1
        if i == 0:
            if 1 in end:
                end[0] = end[1]
                start[end[0]] = 0
                del end[1]
            else:
                start[0] = 0
                end[0] = 0
        elif i == N - 1:
            if N - 2 in start:
                start[N - 1] = start[N - 2]
                end[start[N - 1]] = N - 1
                del start[N - 2]
            else:
                start[N - 1] = N - 1
                end[N - 1] = N - 1
        else:
            if i - 1 in start and i + 1 in end:
                end[start[i - 1]] = end[i + 1]
                start[end[i + 1]] = start[i - 1]
                del start[i - 1]
                del end[i + 1]
            elif i - 1 in start:
                start[i] = start[i - 1]
                end[start[i]] = i
                del start[i - 1]
            elif i + 1 in end:
                end[i] = end[i + 1]
                start[end[i]] = i
                del end[i + 1]
            else:
                start[i] = i
                end[i] = i