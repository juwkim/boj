import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(s):
    i, v = len(s) - 1, 0
    while i >= 0:
        v += s[i] in "aeiou"
        if v == 2:
            break
        i -= 1
    if v != 2:
        return False
    for j in range(i, 0, -1):
        l = len(s) - j
        idx = s.find(s[j:], 0, j)
        if idx == -1:
            continue
        p = s[idx + l:j]
        if any(c in "aeiou" for c in p):
            return True
    return False
for tc in range(1, 1 + int(input())):
    s = input()
    if solve(s) or solve(s[::-1]):
        ans = "Spell!"
    else:
        ans = "Nothing."
    print(f"Case #{tc}: {ans}")