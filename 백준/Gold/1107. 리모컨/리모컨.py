import sys
input = sys.stdin.readline
channel = input().rstrip()
len_channel = len(channel)
M = int(input().rstrip())
not_broken, broken = {*range(10)}, set()
if M > 0:
    broken = {*map(int, input().rstrip().split())}
not_broken -= broken


def solve(N, now):
    global len_channel, channel, minn
    if N > len_channel + 1:
        return
    else:
        if N > len_channel - 2 and N > 0:
            diff = abs(int(channel) - int(now)) + N
            minn = min(minn, diff)
        for btn in not_broken:
            solve(N + 1, now + str(btn))
    
minn = 500000
if channel == '100':
    print(0)
else:
    solve(0, "")
    print(min(minn, abs(100 - int(channel))))