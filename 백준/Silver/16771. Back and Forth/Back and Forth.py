g = lambda: [*map(int, input().split())]

def solve(idx, num, a, b):
    global ans
    if idx == 2:
        ans.add(num)
        return
    for i in range(10):
        tmp = b + [a[i]]
        for j in range(11):
            t = tmp[:j] + tmp[j + 1:]
            s = a[:i] + a[i + 1:] + [tmp[j]]
            solve(idx + 1, num + tmp[j] - a[i], s, t)
ans = set()
solve(0, 0, g(), g())
print(len(ans))