pattern, text = input(), input()
d = {c: [0, 0] for c in "abcdefghijklmnopqrstuvwxyz"}
l = len(text) - len(pattern) + 1
for i in range(l - 1):
    d[text[i]][1] += 1
ans = 0
for i in range(l - 1, len(text)):
    d[text[i]][1] += 1
    c = pattern[i + 1 - l]
    ans += d[c][1] - d[c][0]
    d[text[i + 1 - l]][0] += 1
print(ans)