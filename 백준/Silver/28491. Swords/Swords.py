import sys
input = sys.stdin.readline

ans, prv = 0, 0
for _, b in sorted([[*map(int, input().split())] for _ in range(int(input()))], reverse=True):
    if b > prv:
        prv = b
        ans += 1
print(ans)