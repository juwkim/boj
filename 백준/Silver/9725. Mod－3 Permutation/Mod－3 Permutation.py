import sys
input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    n = int(input())
    cnt = [[0, 0, 0] for _ in range(3)]
    for i, p in enumerate(map(int, input().split())):
        cnt[i % 3][p % 3] += 1
    ans = 0
    for i, j in (0, 1), (0, 2), (1, 2):
        a = min(cnt[i][j], cnt[j][i])
        ans += a
        cnt[i][j] -= a
        cnt[j][i] -= a
    ans += sum(cnt[0][1:]) << 1
    print(f"Case #{tc}: {ans}")