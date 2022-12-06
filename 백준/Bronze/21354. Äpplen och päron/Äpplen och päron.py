A, P = map(int, input().split())
A *= 7
P *= 13
print(['lika', 'Axel', 'Petra'][(A > P) - (A < P)])