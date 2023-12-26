import sys

input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7

def solve(s):
    n = len(s)
    cur = [[[0 for _ in range(4)] for _ in range(n//2 + 2)] for _ in range(n//2 + 2)]
    cur[0][0][0] = 1
    for i in range(n):
        new = [[[0 for _ in range(4)] for _ in range(n//2 + 2)] for _ in range(n//2 + 2)]
        for j in range(n // 2 + 1):
            for k in range(n // 2 + 1):
                if sum(cur[j][k]) == 0:
                    continue
                # situation 0
                new[j][k] = [(a + b) % MOD for a, b in zip(new[j][k], cur[j][k])]
                if s[i] == 'a':
                    new[j + 1][k][0] = (new[j + 1][k][0] + cur[j][k][0]) % MOD
                elif s[i] == 'b' and j > 0:
                    new[j][k + 1][1] = (new[j][k + 1][1] + cur[j][k][0]) % MOD

                if s[i] == 'b':
                    new[j][k + 1][1] = (new[j][k + 1][1] + cur[j][k][1]) % MOD
                elif s[i] == 'c':
                    if j == 1:
                        new[0][k][3] = (new[0][k][3] + cur[j][k][1]) % MOD
                    else:
                        new[j - 1][k][2] = (new[j - 1][k][2] + cur[j][k][1]) % MOD

                if s[i] == 'c':
                    if j == 1:
                        new[0][k][3] = (new[0][k][3] + cur[j][k][2]) % MOD
                    else:
                        new[j - 1][k][2] = (new[j - 1][k][2] + cur[j][k][2]) % MOD

                if s[i] == 'd':
                    if k == 1:
                        new[0][0][0] = (new[0][0][0] + cur[j][k][3]) % MOD
                    else:
                        new[0][k - 1][3] = (new[0][k - 1][3] + cur[j][k][3]) % MOD
        cur = new
    return (cur[0][0][0] - 1) % MOD

for tc in range(1, int(input()) + 1):
    print(f"Case #{tc}: {solve(input())}")