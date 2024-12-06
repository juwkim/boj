import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(s):
    s = " ".join(s.lower().split()).replace("[", "(").replace("{", "(").replace("]", ")").replace("}", ")").replace(";", ",")
    l = []
    for i, c in enumerate(s):
        if c in "().,:":
            if i and s[i - 1] != " ":
                l.append(' ')
            l.append(c)
            if i + 1 < len(s) and s[i + 1] != " ":
                l.append(' ')
        else:
            l.append(c)
    return "".join(l)

for tc in range(1, 1 + int(input())):
    ans = ("not equal", "equal")[solve(input()) == solve(input())]
    print(f"Data Set {tc}: {ans}\n")