def g(): return [*map(int, input().split())]
for _ in range(int(input())):
    input()
    n, q = g()
    px_sum = [0]
    for num in g():
        px_sum.append(px_sum[-1] + num)
    for _ in range(q):
        i, j = g()
        print(px_sum[j + 1] - px_sum[i])
    print()