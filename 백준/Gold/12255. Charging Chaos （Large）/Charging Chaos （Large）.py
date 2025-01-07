import sys
input = sys.stdin.readline
g = lambda: [*map(lambda x: int(x, 2), input().split())]

for tc in range(1, 1 + int(input())):
    N, L = map(int, input().split())
    s, t = g(), g()
    idx = {c: i for i, c in enumerate(t)}
    ans = "NOT POSSIBLE"
    for i in range(N):
        diff = [j for j in range(L) if s[0] & 1 << j != t[i] & 1 << j]
        if type(ans) == int and len(diff) >= ans:
            continue
        visited = bytearray(N)
        visited[i] = 1
        for j in range(1, N):
            cur = s[j]
            for k in diff:
                cur ^= 1 << k
            if cur not in idx or visited[idx[cur]]:
                break
            visited[idx[cur]] = 1
        else:
            ans = len(diff)
    print(f"Case #{tc}: {ans}")