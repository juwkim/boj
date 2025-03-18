import sys
input = sys.stdin.readline

n = int(input())
m = [*map(float, input().split())]
a, q = map(int, input().split())
ans = m[a - 1]
print(f"{ans:.2f}")
cnt, m[a - 1] = n - 1, 0
for _ in range(q):
    cmd, x = input().split()
    if cmd == 'O':
        m[int(x) - 1] = 0
        cnt -= 1
    elif x == 'D':
        ans = 0.9 * sum(m) / cnt
        break
print(f"{ans:.2f}")