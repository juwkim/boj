M, N = map(int, input().split())
t = min(M, N)
a = max(t - 2 - t % 2, 0)

M, N = M - a, N - a

if M == 2:
    s = 2
elif N == 2:
    s = 3
elif M == 3:
    s = 4
else:
    s = 5

print(a // 2 * 4 + s)