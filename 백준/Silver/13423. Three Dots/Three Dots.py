import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    X = sorted(map(int, input().split()))
    s = set(X)
    print(sum(2 * X[j] - X[i] in s for i in range(N - 2) for j in range(i + 1, N - 1)))