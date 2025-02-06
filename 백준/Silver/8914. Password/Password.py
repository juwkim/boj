from itertools import product

for _ in range(int(input())):
    K = int(input())
    A = [*zip(*[input() for _ in range(6)])]
    B = [*zip(*[input() for _ in range(6)])]
    l = sorted(product(*[set(p) & set(q) for p, q in zip(A, B)]))
    if len(l) < K:
        print("NO")
    else:
        print(*l[K - 1], sep="")