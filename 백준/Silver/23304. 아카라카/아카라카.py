def solve(l, r):
    len = r - l + 1
    if len == 1:
        return True
    if any(s[l + i] != s[r - i] for i in range(len // 2)):
        return False
    return solve(l, l + len // 2 - 1) and solve(r - len // 2 + 1, r)

s = input()
print(("IPSELENTI", "AKARAKA")[solve(0, len(s) - 1)])