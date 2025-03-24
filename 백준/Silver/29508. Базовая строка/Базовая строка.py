s, t = input(), input()
a, b = len(s), len(t)
ans = "NO"
for l in range(min(a, b), 0, -1):
    if a % l or b % l:
        continue
    pattern = s[:l]
    if all(pattern[i % l] == s[i] for i in range(l, a)) and all(pattern[i % l] == t[i] for i in range(b)):
        ans = pattern
        break
print(ans)