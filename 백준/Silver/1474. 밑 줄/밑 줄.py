import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
words = [input() for _ in range(N)]
q, r = divmod(M - sum(len(word) for word in words), N - 1)
ans = [words[0]]
for i in range(1, N):
    if r == N - i or r and words[i][0].islower():
        c = '_' * (q + 1)
        r -= 1
    else:
        c = '_' * q
    ans.append(c + words[i])
print(*ans, sep='')