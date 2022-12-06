g = lambda: [*map(int, input().split())]

S, N = g()
buf = [0] * S
for num in g():
    buf[(num - 2) % S] = 1
    buf[num-1] = 1
    buf[num % S] = 1
ans = 0
for i in range(S):
    if buf[i] == 0:
        buf[i] = 1
        buf[(i-1)%S] = 1
        buf[(i+1)%S] = 1
        ans += 1
print(ans)