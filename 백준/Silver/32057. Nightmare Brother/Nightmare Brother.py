import sys
input = sys.stdin.readline

N, M = map(int, input().split())
hints = []
for _ in range(N):
    X, T = input().split()
    hints.append((int(X), T))
def solve(skip):
    s = ['?'] * M
    for i in range(N):
        if i == skip:
            continue
        X, T = hints[i]
        for j in range(len(T)):
            pos = X + j - 1
            if s[pos] == '?':
                s[pos] = T[j]
            elif s[pos] != T[j]:
                return None
    if '?' in s:
        return None
    return ''.join(s)
ans = -1
for i in range(N + 1):
    ret = solve(i)
    if ret is None:
        continue
    if ans == -1:
        ans = ret
    elif ret != ans:
        ans = -2
        break
print(ans)