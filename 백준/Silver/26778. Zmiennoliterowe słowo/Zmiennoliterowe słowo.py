s = input()
ans = sum(a == b for a, b in zip(s, s[1:]))
print(ans)