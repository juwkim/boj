import sys
input = lambda: sys.stdin.readline().rstrip()

n = input()
if len(n) == 1:
    ans = int(n)
else:
    ans = 9 * sum(pow(10, j // 2) for j in range(len(n) - 1))
    l, s = ['0'] * len(n), [*n]
    t = len(l) // 2
    for i in map(lambda x: str(x).zfill(t), range(1, pow(10, t))):
        if i[-1] == '0':
            continue
        l[:t] = i[::-1]
        l[-t:] = i
        if len(n) & 1:
            for j in map(str, range(10)):
                l[t] = j
                if l <= s:
                    ans += 1
        else:
            if l <= s:
                ans += 1
print(ans)