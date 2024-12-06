N, *elsie = map(int, open(0))
elsie.sort()
bessie = list({*range(1, 2 * N + 1)} - set(elsie))
ans, i = 0, 0
for num in elsie:
    while i < N and bessie[i] < num:
        i += 1
    if i == N:
        break
    ans += 1
    i += 1
print(ans)