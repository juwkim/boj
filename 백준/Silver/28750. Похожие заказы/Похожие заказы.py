n = int(input())
t, s = input(), input()
ans = "Impossible"
for k in range(n):
    shifted_s = s[k:] + s[:k]
    d = (ord(shifted_s[0]) - ord(t[0])) % 26
    if all((ord(shifted_s[i]) - ord(t[i])) % 26 == d for i in range(n)):
        ans = f"Success\n{k} {d}"
        break
print(ans)