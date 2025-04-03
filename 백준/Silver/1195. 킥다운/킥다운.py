def solve(s, t):
    i = 0
    while i < len(s):
        if all(s[i+j] + t[j] != "22" for j in range(min(len(s) - i, len(t)))):
            break
        i += 1
    return max(len(s), i + len(t))

a, b = input(), input()
print(min(solve(a, b), solve(b, a)))