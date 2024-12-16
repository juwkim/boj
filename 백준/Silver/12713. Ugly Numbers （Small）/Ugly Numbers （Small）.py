import sys
input = lambda: sys.stdin.readline().strip()

def solve(i, num):
    global ans
    if i == len(s):
        ans += any(num % i == 0 for i in (2, 3, 5, 7))
        return
    cur = 0
    for j in range(i, len(s)):
        cur = cur * 10 + s[j]
        solve(j + 1, num + cur)
        if i:
            solve(j + 1, num - cur)

for tc in range(1, 1 + int(input())):
    s = [*map(int, input())]
    ans = 0
    solve(0, 0)
    print(f"Case #{tc}: {ans}")