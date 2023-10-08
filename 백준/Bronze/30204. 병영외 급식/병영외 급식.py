g = lambda: map(int, input().split())

N, X = g()
print(1 - bool(sum(g()) % X))