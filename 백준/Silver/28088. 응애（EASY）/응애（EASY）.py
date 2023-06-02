N, M, K = map(int, input().split())
s = bytearray(N)
for _ in range(M):
    s[int(input())] = 1
for _ in range(K):
    tmp = bytearray(N)
    for i in range(N):
        if s[(i - 1) % N] + s[(i + 1) % N] == 1:
            tmp[i] = 1
    s = tmp
print(sum(s))