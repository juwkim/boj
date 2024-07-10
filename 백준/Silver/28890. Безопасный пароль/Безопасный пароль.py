from collections import Counter

alpha = "abcdefghijklmnopqrstuvwxyz"
s = [*input()]
a = ({*alpha} - {*s}).pop()
for i in range(2, len(s)):
    if s[i] == s[i - 1] == s[i - 2]:
        s[i] = a
cnt = Counter(s)
k, v = cnt.most_common(1)[0]
if v > len(s) // 2:
    t = v - len(s) // 2
    c = min(alpha, key=lambda x: cnt[x])
    for i in range(len(s)):
        if s[i] == k:
            s[i] = c
            t -= 1
            if t == 0:
                break
print(*s, sep="")