A, B = map(int, [input(), input()])
D = min(abs(A-B), 360 - abs(A-B))
print(D if (A+D)%360 == B else -D)