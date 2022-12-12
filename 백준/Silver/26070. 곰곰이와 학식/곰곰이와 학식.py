g = lambda: [*map(int, input().split())]

p = g()
q = g()
ans = 0
for i in range(3):
    used = min(p[i], q[i])
    p[i] -= used
    q[i] -= used
    q[(i + 1) % 3] += q[i] // 3
    q[i] %= 3
    ans += used

for i in range(3):
    used = min(p[i], q[i])
    p[i] -= used
    q[i] -= used
    q[(i + 1) % 3] += q[i] // 3
    q[i] %= 3
    ans += used

print(ans)