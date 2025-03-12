import sys
input = sys.stdin.readline

n = int(input())
p = [[' '] * 211 for _ in range(2 * n + 1)]
for i in range(2 * n + 1): p[i][0] = '+|'[i & 1]
for i in range(1, 2 * n, 2):
    m, *a = map(int, input().split())
    j = 0
    for x in a:
        j += x + 1
        p[i][j] = '|'
        p[i - 1][j] = '+'
        p[i + 1][j] = '+'
for i in range(0, 2 * (n + 1), 2):
    j = 210
    while p[i][j] == ' ': j -= 1
    while j:
        if p[i][j] == ' ':
            p[i][j] = '-'
        j -= 1
for l in p:
    print("".join(l).rstrip())