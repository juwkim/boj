import sys

input = sys.stdin.read
data = input().split()

n, w, h = map(int, data[:3])
offset = 3
rocks = [data[offset + i * h : offset + (i + 1) * h] for i in range(n)]
key = data[offset + n * h : offset + (n + 1) * h]

ans = 0
for rock in rocks:
    valid = True
    for l in range(1, w + 1):
        found = False
        for i in range(h):
            for j in range(l):
                if rock[i][j] == '#' and key[i][w + j - l] == '#':
                    found = True
                    break
            if found:
                break
        if found:
            valid = False
            break
    if valid:
        ans += 1

print(ans)