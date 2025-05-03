import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    n, m = map(int, input().split())
    datasets = [int(input(), 2) for _ in range(m)]
    targets = (1 << n) - 1
    ans = float('inf')
    for subset in range(1, 1 << m):
        combined, cnt = 0, 0
        for i in range(m):
            if (subset >> i) & 1:
                combined |= datasets[i]
                cnt += 1
                if cnt == ans:
                    break
        if combined == targets and cnt < ans:
            ans = cnt
    print(-1 if ans == float('inf') else ans)