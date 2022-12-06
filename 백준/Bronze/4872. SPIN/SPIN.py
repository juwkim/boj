import sys
ans = [0] * 10
N = 0
for line in sys.stdin:
    N = len(line) - 1
    for idx, num in enumerate(line.rstrip()):
        ans[idx] += int(num)
print(*[ans[i] % 10 for i in range(N)], sep='')