n, k, p = map(int, input().split())
Continue = (n - k) + 1 + (3 + n + 1) * p / 100
Backspace = 1 + (n - k) + 1 + (3 + n + 1) * (100 - p) / 100
Restart = 3 + n + 1
ans = min(Continue, Backspace, Restart)
if ans == Continue:
    print("continue")
elif ans == Backspace:
    print("backspace")
else:
    print("restart")