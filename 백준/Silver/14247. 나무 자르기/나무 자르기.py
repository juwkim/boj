g = lambda: [*map(int, input().split())]

n = int(input())
H, A = g(), g()
print(sum(d * A[i] + H[i] for d, i in enumerate(sorted(range(n), key=lambda x: A[x]))))