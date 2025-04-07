import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    ans, dp = 0, []
    for w, c in [[*map(float, input().split())] for _ in range(N)]:
        cur = 1
        for w0, c0, cnt0 in dp:
            if w > w0 and c < c0:
                cur = max(cur, cnt0 + 1)
        dp.append((w, c, cur))
        ans = max(ans, cur)
    print(ans)