s = input()
m = int(input())
ans = 0
for c in map(chr, range(97, 123)):
    l, r, cnt = 0, 0, 0
    while r < len(s):
        if s[r] == c:
            r += 1
            ans = max(ans, r - l - cnt)
        elif cnt == m:
            cnt -= s[l] != c
            l += 1
        else:
            cnt += s[r] != c
            r += 1
print(ans)