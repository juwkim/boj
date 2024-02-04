import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import product

def solve(s, l, r, truth_table):
    if l == r:
        if s[l] == 'T':
            return True
        if s[l] == 'F':
            return False
        return truth_table[idx[s[l]]]
    if s[l] == '-':
        return not solve(s, l + 1, r, truth_table)
    st = 0
    for i in range(l, r + 1):
        if s[i] == '(':
            st += 1
        elif s[i] == ')':
            st -= 1
        if st != 1:
            continue
        if s[i] == '*':
            return solve(s, l + 1, i - 1, truth_table) and solve(s, i + 1, r - 1, truth_table)
        elif s[i] == '+':
            return solve(s, l + 1, i - 1, truth_table) or solve(s, i + 1, r - 1, truth_table)
        elif s[i:i+2] == '->':
            return not solve(s, l + 1, i - 1, truth_table) or solve(s, i + 2, r - 1, truth_table)
            
while (line:=input()) != '#':
    a, b = line.split('=')
    alpha = set(c for c in line if c.islower())
    idx = {c: i for i, c in enumerate(alpha)}
    if all(solve(a, 0, len(a) - 1, truth_table) == solve(b, 0, len(b) - 1, truth_table) for truth_table in product([True, False], repeat=len(alpha))):
        print('YES')
    else:
        print('NO')