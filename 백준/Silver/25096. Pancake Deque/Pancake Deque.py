import sys
input = sys.stdin.readline

for tc in range(1, 1 + int(input())):
    l, r = 0, int(input()) - 1
    D = [*map(int, input().split())]
    ans, prv = 0, 0
    while l <= r:
        if D[l] < D[r]:
            cur = D[l]
            l += 1
        else:
            cur = D[r]
            r -= 1
        if cur >= prv:
            ans += 1
            prv = cur
    print(f'Case #{tc}: {ans}')