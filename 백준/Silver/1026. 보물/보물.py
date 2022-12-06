g = lambda: [*map(int, input().split())]

N = int(input())
A = sorted(g())
B = sorted(g(), reverse=True)
print(sum(a * b for a, b in zip(A, B)))