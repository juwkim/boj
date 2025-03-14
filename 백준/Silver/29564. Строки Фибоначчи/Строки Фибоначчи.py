import sys
input = sys.stdin.readline

fibo = [1, 1]
for i in range(42):
    fibo.append(fibo[-1] + fibo[-2])

for _ in range(int(input())):
    n, k = map(int, input().split())
    def solve(i, j):
        if i == 0:
            return 'a'
        if i == 1:
            return 'b'
        if j <= fibo[i - 2]:
            return solve(i - 2, j)
        return solve(i - 1, j - fibo[i - 2])
    print(solve(n, k))