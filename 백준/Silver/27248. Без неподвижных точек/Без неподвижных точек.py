n, t = map(int, input().split())
used = bytearray(n + 1)
ans, out = [], []
def solve(pos):
    global t
    if pos > n:
        print(*ans)
        t -= 1
        return
    for i in range(1, n + 1):
        if not used[i] and i != pos:
            used[i] = True
            ans.append(i)
            solve(pos + 1)
            if t == 0:
                return
            ans.pop()
            used[i] = False
solve(1)