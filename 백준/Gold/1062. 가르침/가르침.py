import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K = g()
if K < 5:
    print(0)
else:
    words = [list(set(ord(i) - ord('a') for i in input()[4:-4])) for _ in range(N)]
    check = [0] * 26
    for i in map(ord, 'antic'):
        check[i - ord('a')] = 1
    ans = 0
    def solve(idx, cnt):
        global ans
        if cnt == K - 5:
            tmp = sum(all(check[c] for c in word) for word in words)
            ans = max(ans, tmp)
            return
        for i in range(idx, 26):
            if not check[i]:
                check[i] = 1
                solve(i + 1, cnt + 1)
                check[i] = 0
    solve(0, 0)
    print(ans)