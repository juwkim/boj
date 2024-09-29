import sys
input = sys.stdin.readline

N = int(input())
K = [[*map(int, input().split())] for _ in range(N)]
ans = 3
for i in range(3):
    if all(all(l[i] < l[i + 1] for i in range(N - 1)) for l in K) and all(all(l[i] < l[i + 1] for i in range(N - 1)) for l in [*zip(*K)]):
        ans = i
        break
    K = [*zip(*K)][::-1]
print(ans)