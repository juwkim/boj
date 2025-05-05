import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    valid = set(s)
    for i in range(n):
        for j in range(n):
            z = t[i][j]
            if z not in valid:
                return f"NOT A SEMIGROUP: {s[i]}#{s[j]} = {z}  WHICH IS NOT AN ELEMENT OF THE SET"
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if t[idx[t[x][y]]][z] != t[x][idx[t[y][z]]]:
                    return f"NOT A SEMIGROUP: ({s[x]}#{s[y]})#{s[z]} IS NOT EQUAL TO {s[x]}#({s[y]}#{s[z]})"
    for i in range(n - 1):
        for j in range(i + 1, n):
            if t[i][j] != t[j][i]:
                return f"SEMIGROUP BUT NOT COMMUTATIVE  ({s[i]}#{s[j]} IS NOT EQUAL TO {s[j]}#{s[i]})"
    return "COMMUTATIVE SEMIGROUP"

while n:=int(input()):
    s = input()
    idx = {c: i for i, c in enumerate(s)}
    t = [input() for _ in range(n)]
    print(f"S = {{{','.join(s)}}}")
    print(f" #|{s}")
    print(f" -+{'-' * n}")
    for i in range(n):
        print(f" {s[i]}|{t[i]}")
    print()
    print(solve())
    print('-' * 30)
    print()