import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def solve():
    s, f = input().lower(), input().lower()
    i, j = 0, 0
    while i < len(s) and j < len(f):
        if s[i] == f[j]:
            i += 1
            j += 1
        elif f[j] in 'aeiouy':
            j += 1
        else:
            return "Different"
    
    if i == len(s) and (j == len(f) or all(c in 'aeiouy' for c in f[j:])):
        return "Same"
    return "Different"

print(solve())