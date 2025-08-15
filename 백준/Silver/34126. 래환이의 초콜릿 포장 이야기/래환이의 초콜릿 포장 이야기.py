import sys
input = sys.stdin.readline

for _ in range(int(input())):
    A, B, C = map(int, input().split())
    ans = (C + 1) // 2 * 3
    cnt = A + 2 * B
    if C & 1:
        cnt -= 3
    ans += max(0, cnt + 1 >> 1)
    print(ans)