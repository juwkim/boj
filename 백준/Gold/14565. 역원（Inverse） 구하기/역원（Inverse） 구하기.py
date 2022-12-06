g = lambda: [*map(int, input().split())]
N, A = g()
try:
    print(N - A, pow(A, -1, N))
except:
    print(N - A, -1) 