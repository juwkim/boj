g = lambda: [*map(int, input().split())]
N = int(input())
buf = []
for _ in range(N):
    buf.append(sorted(g())[N//2])
print(sorted(buf)[N//2])