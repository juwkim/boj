N, O = map(int, [input(), input()])
X = [*filter(lambda x: x==int(x), [(N*O - a)/(N - 1) for a in range(N)])]
print(int(X[-1]), int(X[0]))