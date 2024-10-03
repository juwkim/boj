def solve(l, r):
    return r == l or all(s[l + i] == s[r - i] for i in range((r - l + 1) // 2)) and solve(l, (r + l - 1) // 2) and solve((r + l + 2) // 2, r)
s = input()
print(("IPSELENTI", "AKARAKA")[solve(0, len(s) - 1)])