import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    k1, k2, k3 = map(int, input().split())
    if k1 == 0:
        break
    s = input()
    ans = [''] * len(s)
    idx = [i for i in range(len(s)) if 'a' <= s[i] <= 'i']
    for i in range(len(idx)):
        ans[idx[i]] = s[idx[(i - k1) % len(idx)]]
    idx = [i for i in range(len(s)) if 'j' <= s[i] <= 'r']
    for i in range(len(idx)):
        ans[idx[i]] = s[idx[(i - k2) % len(idx)]]
    idx = [i for i in range(len(s)) if 's' <= s[i] <= 'z' or s[i] == '_']
    for i in range(len(idx)):
        ans[idx[i]] = s[idx[(i - k3) % len(idx)]]
    print(*ans, sep='')