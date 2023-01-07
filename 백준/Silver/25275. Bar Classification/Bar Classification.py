N = int(input())
mat = [input() for _ in range(N)]

ones = [line.count('1') for line in mat]
total = sum(ones)

ans = 0
if any(total - one + N - one <= N for one in ones):
    ans += 1

ones = [line.count('1') for line in zip(*mat)]
total = sum(ones)

if any(total - one + N - one <= N for one in ones):
    ans += 2

print(' -|+'[ans])