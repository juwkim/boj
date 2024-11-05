import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

N = int(input())
Min = Max = g()
for _ in range(N - 1):
    a, b, c = g()
    Min = a + min(Min[0], Min[1]), b + min(Min), c + min(Min[1], Min[2])
    Max = a + max(Max[0], Max[1]), b + max(Max), c + max(Max[1], Max[2])
print(max(Max), min(Min))