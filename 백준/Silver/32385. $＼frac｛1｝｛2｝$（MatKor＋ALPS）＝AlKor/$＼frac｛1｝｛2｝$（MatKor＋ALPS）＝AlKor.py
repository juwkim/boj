N = int(input())
q, r = divmod(N, 2)
if r:
    ans = [*range(1, q), *range(-q + 1, 0), q, (q + 1), -2*q - 1, 0]
else:
    ans = [*range(1, q + 1), *range(-q, 0), 0]
print(*ans)