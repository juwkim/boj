a, b = input(), input()
N = len(a)
s = sorted(a, reverse=True)[-((N + 1) // 2):]
t = sorted(b)[-(N // 2):]
i = 0
while i < N and not (s and t and s[-1] >= t[-1]):
    print(t.pop() if i&1 else s.pop(), end='')
    i += 1
s, t = s[::-1], t[::-1]
ans = [t.pop() if j&1 else s.pop() for j in range(i, N)][::-1]
print(*ans, sep='')