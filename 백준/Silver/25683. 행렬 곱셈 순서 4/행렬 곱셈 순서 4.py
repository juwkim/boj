import sys
input = sys.stdin.readline

N = int(input())
r, c = zip(*[[*map(int, input().split())] for _ in range(N)])
print(sum(r[i] * r[i + 1] for i in range(N - 1)) * c[-1])