def solve():
    used = bytearray(N)
    rank = 1
    for i, c in enumerate(input()):
        idx = ord(c) - ord('a')
        rank += sum(not used[j] for j in range(idx)) * fact[N - 1 - i]
        used[idx] = True
    return rank

N = int(input())
fact = [1] * (N + 1)
for i in range(2, N + 1):
    fact[i] = fact[i - 1] * i
print(abs(solve() - solve()))