import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    ans, cur = 0, 0
    for S, C in zip(map(int, input().split()), input().split()):
        if C == 'T':
            cur += S
        else:
            cur -= S
        ans = max(ans, cur)
    print(ans)