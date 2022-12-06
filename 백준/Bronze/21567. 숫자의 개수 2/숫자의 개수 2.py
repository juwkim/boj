from collections import Counter
A, B, C = map(int, [input() for _ in range(3)])
res = Counter(str(A * B * C))
for i in range(10):
    print(res[str(i)])