from collections import Counter

cnt = Counter(s:=input())
ans = 0
def solve(i, c):
    global ans
    if i == len(s):
        ans += 1
        return
    for k, v in cnt.items():
        if v > 0 and k != c:
            cnt[k] -= 1
            solve(i + 1, k)
            cnt[k] += 1
if len(cnt) == 10:
    print(3628800)
else:
    solve(0, '')
    print(ans)