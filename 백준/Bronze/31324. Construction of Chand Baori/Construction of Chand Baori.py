N, M = map(int, input().split())
cur = 1
for i in range(2, 2 * (N + 1), 2):
    cur *= i
if cur >= M:
    print("Harshat Mata")
else:
    print("Nope")